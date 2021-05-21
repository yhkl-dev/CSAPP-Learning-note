package Map

import (
	"fmt"
	"sort"
)

type User map[string]interface{}

func NewUser() User {
	return make(User)
}

func (u User) With(k string, v interface{}) User {
	u[k] = v
	return u
}

func (u User) Fields() []string {
	keys := []string{}
	for k := range u {
		keys = append(keys, k)
	}
	sort.Sort(sort.Reverse(sort.StringSlice(keys)))
	return keys
}

func (u User) String() string {
	str := ""
	for index, k := range u.Fields() {
		str += fmt.Sprintf("%d: %v->%v\n", index+1, k, u[k])
	}
	return str
}
