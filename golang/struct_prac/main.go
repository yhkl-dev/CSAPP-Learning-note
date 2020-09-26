package main

import "fmt"

type UserModel struct {
	uid   int
	uname string
}

func (this UserModel) ToString() string {
	return "user id" + this.uname
}

func (this *UserModel) SetValue(id int, name string) {
	this.uid = id
	this.uname = name
}

func main() {
	user := UserModel{uid: 1, uname: "yhkl"}
	fmt.Println(user.ToString())

	user.SetValue(2, "tina")

	fmt.Println(user.ToString())

	fmt.Println("vim-go")

	var name *string
	name = new(string)

	*name = "yhkl"
	fmt.Println(*name)
}
