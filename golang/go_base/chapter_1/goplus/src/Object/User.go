package Object

type User struct {
	Id   int
	Sex  int
	Name string
}

func WithUserID(id int) func(u *User) {
	return func(u *User) {
		u.Id = id
	}
}

func NewUser(f func(u *User)) *User {
	u := new(User)
	f(u)
	return u
}
