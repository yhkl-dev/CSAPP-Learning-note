package main

import (
	"flag"
	"fmt"
)

func main() {
	//	var file = flag.String("f", "/root/.vimrc", "the file name")
	var fileName string
	flag.StringVar(&fileName, "f", "/root/.vimrc", "the file name new")
	var newLineMark bool

	flag.BoolVar(&newLineMark, "m", false, "是否换行")

	flag.Parse()
	//	fmt.Println("the file name is: ", *file)
	if newLineMark {
		fmt.Println()
	}
	fmt.Println("the file name is: ", fileName)
}
