package main

import (
	"fmt"
	"io"
	"log"
	"net"

	cprng "crypto/rand"
	"encoding/binary"
	"github.com/adamyi/guess_ctf_challenge/guess/flag"
	pb "github.com/adamyi/guess_ctf_challenge/guess/proto"
	"google.golang.org/grpc"
	"math/rand"
)

const (
	port        = ":80"
	randomlevel = 100
	maxtries    = 6843
	maxnums     = 6443
	maxnum      = 9447
)

type server struct{}

func NewNum(r *rand.Rand) int64 {
	ret := r.Int63() % maxnum
	return ret
}

// we generate seed recursively
// this makes us super safe
func NewRandomizer(randomness int) (*rand.Rand, error) {
	var seed int64
	if randomness == 0 {
		if err := binary.Read(cprng.Reader, binary.LittleEndian, &seed); err != nil {
			return nil, fmt.Errorf("couldn't read random int64: %v", err)
		}
	} else {
		r, err := NewRandomizer(randomness - 1)
		if err != nil {
			return nil, fmt.Errorf("couldn't init new randomizer: %v", err)
		}
		seed = NewNum(r)
	}
	return rand.New(rand.NewSource(seed)), nil
}

func (s server) PlayGame(srv pb.Guess_PlayGameServer) error {
	log.Println("play new game")
	ctx := srv.Context()
	r, err := NewRandomizer(randomlevel)
	if err != nil {
		log.Printf("random init er %v", err)
		return nil
	}
	nums := maxnums
	tries := maxtries
	n := NewNum(r)
	cont := true
	var captcha int64
	for cont {
		// exit if context is done
		// or continue
		select {
		case <-ctx.Done():
			return ctx.Err()
		default:
		}

		// receive data from stream
		req, err := srv.Recv()
		if err == io.EOF {
			// return will close stream from server side
			log.Println("exit")
			return nil
		}
		if err != nil {
			log.Printf("receive error %v", err)
			continue
		}

		log.Printf("Got %d", req.Num)

		tries -= 1

		var status string

		if req.Num == n {
			status = "CORRECT"
			nums -= 1
			if nums == 0 {
				status += ". CONGRATULATIONS! YOUR FLAG IS " + flag.Flag
				cont = false
			} else {
				n = NewNum(r)
			}
		} else if req.Num < n {
			status = "TOO SMALL"
		} else {
			status = "TOO LARGE"
		}

		if tries == 0 {
			status += ". YOU'VE USED UP ALL TRIES."
			cont = false
		}

		if req.Captcha != captcha {
			status = "WRONG CAPTCHA. ARE YOU TRYING TO CRACK MY SOFTWARE?"
			cont = false
			// this way they don't know if their last guess is correct or not
			nums = maxnums
			tries = 0
		}

		msg := fmt.Sprintf("%d is %s", req.Num, status)
		cap1 := rand.Int31() / 10
		cap2 := rand.Int31() / 10
		captcha = int64(cap1) * int64(cap2)
		resp := pb.GuessReply{Msg: msg, Tries: int32(tries), Nums: int32(nums), Captcha1: cap1, Captcha2: cap2, Done: !cont}
		if err := srv.Send(&resp); err != nil {
			log.Printf("send error %v", err)
		}
	}
	return nil
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterGuessServer(s, server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
