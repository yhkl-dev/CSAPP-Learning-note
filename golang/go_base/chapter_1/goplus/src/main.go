package main

import (
	"fmt"
	"goplus/goplus/src/Object"
)

func change(u Object.User) Object.User {
	u.Id = 202

	return u
}

func main() {
	/*
		s := String.NewString("abc上开")
		fmt.Println(s)
		fmt.Println("vim-go")
		s1 := String.FromInt(123)
		fmt.Println(s1)

		fmt.Println(s1.Len())

		s.Each(func(item string) {
			fmt.Println(item)
		})

		for i := 0; i < len(s); i++ {
			fmt.Println(i, " ", s[i], fmt.Sprintf("%T", s[i]))
		}

		fmt.Println([]byte(s))
		fmt.Println([]int32(s))
		fmt.Printf("%c\n", 24320)

		u := Object.NewUser()
		fmt.Println(u)
		u.Id = 101
		u = change(u)
		fmt.Printf("%+v", u)
	*/

	u := Object.NewUser(
		Object.WithUserID(120),
	)
	fmt.Println(u)
}
