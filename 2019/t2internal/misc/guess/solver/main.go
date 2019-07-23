package main

import (
	"io"
	"log"
	"strings"

	pb "github.com/adamyi/guess_ctf_challenge/guess/proto"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
	"math/rand"
)

const (
	address = "guess-a-number-and-get-a-flag.nsa.group:80"
	maxnum  = 9447
	bsnums  = 5
)

func NewNum(r *rand.Rand) int64 {
	ret := r.Int63() % maxnum
	return ret
}

func NewRandomizer(seed int64) *rand.Rand {
	return rand.New(rand.NewSource(seed))
}

func BinSearch(stream pb.Guess_PlayGameClient, minv int, maxv int, captcha int64) (int, int64) {
	val := (minv + maxv) / 2
	req := pb.GuessRequest{Num: int64(val), Captcha: captcha}
	log.Printf("Sending to server...")
	if err := stream.Send(&req); err != nil {
		log.Fatalf("can not send %v", err)
	}

	resp, err := stream.Recv()
	if err != nil {
		log.Fatalf("can not receive %v", err)
	}
	captcha = int64(resp.Captcha1) * int64(resp.Captcha2)

	log.Println(resp.Msg)
	if strings.Contains(resp.Msg, "CORRECT") {
		return val, captcha
	} else if strings.Contains(resp.Msg, "SMALL") {
		return BinSearch(stream, val+1, maxv, captcha)
	} else {
		return BinSearch(stream, minv, val-1, captcha)
	}
}

func main() {
	/* init random dictionary */
	var dictnums [maxnum][bsnums]int
	var r *rand.Rand
	for i := 0; i < maxnum; i++ {
		r = NewRandomizer(int64(i))
		for j := 0; j < bsnums; j++ {
			dictnums[i][j] = int(NewNum(r))
		}
	}

	/* establish connection */
	conn, err := grpc.Dial(address, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	client := pb.NewGuessClient(conn)
	stream, err := client.PlayGame(context.Background())
	if err != nil {
		log.Fatalf("open stream error %v", err)
	}
	stream.Context()
	done := make(chan bool)
	var captcha int64

	/* binary search first few numbers */
	var mynums [bsnums]int
	for i := 0; i < bsnums; i++ {
		mynums[i], captcha = BinSearch(stream, 0, maxnum-1, captcha)
	}

	/* find random seed */
	for i := 0; i < maxnum; i++ {
		found := true
		for j := 0; j < bsnums; j++ {
			if dictnums[i][j] != mynums[j] {
				found = false
				break
			}
		}
		if found {
			r = NewRandomizer(int64(i))
			for j := 0; j < bsnums; j++ {
				NewNum(r)
			}
			break
		}
	}

	/* win the game */
	for true {
		req := pb.GuessRequest{Num: NewNum(r), Captcha: captcha}
		if err := stream.Send(&req); err != nil {
			log.Fatalf("can not send %v", err)
		}

		resp, err := stream.Recv()
		captcha = int64(resp.Captcha1) * int64(resp.Captcha2)
		if err == io.EOF {
			close(done)
			return
		}
		if err != nil {
			log.Fatalf("can not receive %v", err)
		}

		log.Printf("%s, %d more to go", resp.Msg, resp.Nums)
		if strings.Contains(resp.Msg, "FLAG") {
			break
		}
	}
}
