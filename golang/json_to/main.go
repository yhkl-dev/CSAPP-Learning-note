package main

import (
	"fmt"
	"log"

	"github.com/pquerna/ffjson/ffjson"
)

type Model struct {
	NewsID    int
	NewsTitle string
}

func main() {

	news := Model{123, "title"}
	result, err := ffjson.Marshal(news)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(string(result))
	fmt.Println("vim-go")
}
