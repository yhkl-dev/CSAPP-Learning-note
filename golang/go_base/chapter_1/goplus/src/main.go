package main

import (
	"fmt"
	"reflect"
)

type User struct {
	UserId   int
	UserName string
}

func main() {
	// // u := User{1, "yhkl"}
	// u := User{}
	// t := reflect.TypeOf(u)
	// if t.Kind() == reflect.Ptr {
	// 	t = t.Elem()
	// }
	// // fmt.Println(t.Name())
	// for i := 0; i < t.NumField(); i++ {
	// 	fmt.Println(t.Field(i).Name)
	// }

	// u1 := &User{1, "yhkl"}
	// t1 := reflect.TypeOf(u1)
	// if t1.Kind() == reflect.Ptr {
	// 	t1 = t1.Elem()
	// }
	// // fmt.Println(t.Name())
	// for i := 0; i < t1.NumField(); i++ {
	// 	fmt.Println(t1.Field(i).Name)
	// }
	// t2 := reflect.ValueOf(u)
	// for i := 0; i < t2.NumField(); i++ {
	// 	if t2.Field(i).Kind() == reflect.Int {
	// 		fmt.Println(t2.Field(i).Int())
	// 	}
	// 	if t2.Field(i).Kind() == reflect.String {
	// 		fmt.Println(t2.Field(i).String())
	// 	}
	// 	fmt.Println(t2.Field(i).Interface())
	// }
	// fmt.Println(u)

	u := &User{}
	t := reflect.ValueOf(u)
	if t.Kind() == reflect.Ptr {
		t = t.Elem()
	}

	values := []interface{}{2, "yhkl"}
	for i := 0; i < t.NumField(); i++ {
		if t.Field(i).Kind() == reflect.ValueOf(values[i]).Kind() {
			t.Field(i).Set(reflect.ValueOf(values[i]))
		}
	}
	fmt.Println(u)

}
