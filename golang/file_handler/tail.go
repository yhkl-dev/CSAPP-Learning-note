package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

func main() {
	filename := os.Args[1]

	// f, _ := os.OpenFile(filename, os.O_RDONLY, 0644)
	f, _ := os.Open(filename)

	f.Seek(2, os.SEEK_END)
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
