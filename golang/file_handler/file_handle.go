package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"reflect"
)

func main() {
	if len(os.Args) <= 1 {
		fmt.Println("Usage: go run file_handle.go <filename>")
		os.Exit(1)
	}
	filename := os.Args[1]
	f, err := os.Open(filename)

	fmt.Println("type of f:", reflect.TypeOf(f))
	if err != nil {
		log.Fatal(err)
	}
	r := bufio.NewReader(f)
	for {
		line, err := r.ReadString('\n')
		if err == io.EOF {
			break
		}
		fmt.Print(line)
	}
	f.Close()
}
