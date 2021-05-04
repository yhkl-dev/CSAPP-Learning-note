package main

import "fmt"

/*
	go struct 能不能比较，
	可以也不可以
*/

type User struct {
	Id int
	m  map[string]string
}

type User2 struct {
	Id int
}
type User1 struct {
	Id int
}

func main() {
	a := User{Id: 10}
	b := User{Id: 10}
	// 换成指针使false
	fmt.Println(a == b)
	c := User2{Id: 10}
	d := User1{Id: 10}
	// 换成指针使false
	fmt.Println(c == User2(d))
}
