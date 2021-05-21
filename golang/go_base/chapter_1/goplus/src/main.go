package main

import (
	"fmt"
	"goplus/src/Map"
	"goplus/src/Object"
	"sort"
)

// func change(u Object.User) Object.User {
// 	u.Id = 202

// 	return u
// }

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
		Object.WithUserName("yhkl"),
	)
	fmt.Println(u)

	u1 := Map.NewUser()
	u1.With("name", "weaponX").With("id", 100)

	u2 := Map.NewUser()
	u2.With("name", "yhkl").With("id", 101)

	u3 := Map.NewUser()
	u3.With("name", "xxx").With("id", 102)
	users := []Map.User{}
	users = append(users, u1, u2, u3)
	sort.SliceStable(users, func(i, j int) bool {
		id1 := users[i]["id"].(int) // 断言
		id2 := users[j]["id"].(int) // 断言
		return id1 < id2
	})
	fmt.Println(users)

}
