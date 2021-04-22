package Object

type User struct {
	Id   int
	Sex  int
	Name string
}

func NewUser() User {
	return User{}
}
