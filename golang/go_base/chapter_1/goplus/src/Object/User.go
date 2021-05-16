package Object

type User struct {
	Id   int
	Sex  int
	Name string
}

func UserWithID(id int) func(u *User) {
	return func(u *User) {
		u.Id = id
	}
}

func NewUser() *User {
	return &User{}
}
