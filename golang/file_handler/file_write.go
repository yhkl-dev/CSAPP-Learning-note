package main

import (
	"log"
	"os"
)

func main() {
	//	f, err := os.Create("test.txt")

	f, err := os.OpenFile("a.txt", os.O_CREATE|os.O_APPEND|os.O_RDWR, 0644)

	if err != nil {
		log.Fatal(err)
	}
	f.WriteString("hello world\n")
	f.Close()

}
