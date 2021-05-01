package main

import "fmt"

const (
	Mem = iota
	Adm
)

type User interface {
	GetRole() string
}

type Member struct{}

func (m *Member) GetRole() string {
	return "会员"
}

type Admin struct{}

func (m *Admin) GetRole() string {
	return "后台管理用户"
}

func showUser(u User) {

}
func createUser(t int) User {
	switch t {
	case Mem:
		return new(Member)
	case Adm:
		return new(Admin)
	default:
		return new(Member)
	}

}

func main() {
	fmt.Println("vim-go")
	fmt.Println(createUser(Mem).GetRole())
}
