package main

import (
	"fmt"
	"io"
	"log"
	"time"

	pb "github.com/adamyi/guess_ctf_challenge/guess/proto"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
)

const (
	address = "guess-a-number-and-get-a-flag.nsa.group:80"
)

func main() {
	fmt.Println("Welcome to Guess Trial Client")
	fmt.Println("I added lots of sleep in this client so that I can comment them out in the next version and say I optimized the speed for the next version. This way I can get paid more.")
	fmt.Println("Since this is a trial version, you only have 20 tries with this client despite what the server says.")
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

	for i := 0; i < 20; i++ {
		var n int64
		fmt.Printf("Guess a number between 0 and 9447: ")
		_, err := fmt.Scanf("%d", &n)
		if err != nil {
			log.Fatalf("can not input %v", err)
		}
		if i*i > 370 {
			// to be extra safe
			captcha += n / 7
		}
		req := pb.GuessRequest{Num: n, Captcha: captcha}
		log.Printf("Sending to server...")
		time.Sleep(1 * time.Second)
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
		log.Printf("Waiting for response...")
		time.Sleep(1 * time.Second)
		log.Println(resp.Msg)
		if resp.Done {
			break
		}
		log.Printf("You need to guess %d more numbers in %d tries. \n", resp.Nums, resp.Tries)
	}
	log.Println("You've used up all your 20 tries for the trial version")
	log.Println("Go write your own client (our server is free) or pay to upgrade")
}
