package main

import "fmt"

func main() {

	a1 := [3]int{1, 2, 3}
	fmt.Println(a1)

	var a2 [3]int
	a2 = a1
	fmt.Println(a2)
	fmt.Println(a1 == a2)

	//	a3 := [3]int{1, 2}
	//	a4 := [2]int{1, 2}
	//	fmt.Println(a3 == a4)
}
