package main

import (
	"bytes"
	"fmt"
)

type Empty struct{}
type Set map[interface{}]Empty

func (s Set) Add(vs ...interface{}) Set {
	for _, v := range vs {
		s[v] = Empty{}
	}
	return s
}

func (s Set) String() string {
	var buf bytes.Buffer
	for k, _ := range s {
		if buf.Len() > 0 {
			buf.WriteString(",")
		}
		buf.WriteString(fmt.Sprintf("%v", k))
	}
	return buf.String()
}
func NewSet() Set {
	return make(map[interface{}]Empty)
}

func main() {
	fmt.Println("vim-go")
	set := NewSet().Add(1, 2, 3, 4, 5, 5, 5, 1)
	fmt.Println(set)
}
