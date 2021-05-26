package main

import "fmt"

/*
	go里面没有enum

	提代方法是使用iota

	iota是go语言的常量计数器，只能在常量的表达式中使用(const)
	iota在const关键子出现时将被重置为0（const内部的第一行之前）, const中每新增一行常量声明将使iota计数一次
*/

type UserType int

func (u UserType) String() string {
	switch u {

	case 0:
		return "student"
	case 1:
		return "teacher"
	case 2:
		return "leader"
	}
	return "3"
}

const (
	Student UserType = iota
	_
	Teacher = "a"
	Leader  = iota
)

func main() {
	fmt.Println(UserType(Student), Teacher, UserType(Leader))
}
