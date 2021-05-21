package Object

type User struct {
	Id   int
	Sex  int
	Name string
}

func NewUser(fs ...UserAttrFunc) *User {
	u := new(User)
	UserAttrFuncs(fs).apply(u)
	return u
}
