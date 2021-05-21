package Object

// UserAttrs 设置User属性
type UserAttrFunc func(*User)
type UserAttrFuncs []UserAttrFunc

func (uaf UserAttrFuncs) apply(u *User) {
	for _, f := range uaf {
		f(u)
	}
}
func WithUserID(id int) UserAttrFunc {
	return func(u *User) {
		u.Id = id
	}
}

func WithUserName(name string) UserAttrFunc {
	return func(u *User) {
		u.Name = name
	}
}
