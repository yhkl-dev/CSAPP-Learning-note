package main

import (
	"fmt"
	"unsafe"
)

func main() {

	var r [3]int = [3]int{1, 2, 3}
	fmt.Println("r: %v, len: %d, size: %v\n", r, len(r), unsafe.Sizeof(r))

	var a [3]int = [3]int{1, 2}
	fmt.Println("r: %v, len: %d, size: %v\n", a, len(a), unsafe.Sizeof(a))

	b := [...]int{1, 2, 3}
	fmt.Println("b: %v, len: %d, size: %v\n", b, len(b), unsafe.Sizeof(b))

	c := [...]int{0: 1, 2: 3}
	fmt.Println("c: %v, len: %d, size: %v\n", c, len(c), unsafe.Sizeof(c))

}
