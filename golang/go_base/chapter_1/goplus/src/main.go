package main

import (
	"fmt"
	"goplus/goplus/src/String"
)

func main() {
	s := String.NewString("abc")
	fmt.Println(s)
	fmt.Println("vim-go")
	s1 := String.FromInt(123)
	fmt.Println(s1)

	fmt.Println(s1.Len())
}
