package main

import (
	"fmt"
	"reflect"
)

type User struct {
	UserId   int
	UserName string
}

func Map2Struct(m map[string]interface{}, u interface{}) {
	v := reflect.ValueOf(u)
	if v.Kind() == reflect.Ptr {
		v = v.Elem()
		if v.Kind() != reflect.Struct {
			panic("must be struct")
		}
		findFromMap := func(key string) interface{} {
			for k, v := range m {
				if k == key {
					return v
				}
			}
			return nil
		}
		for i := 0; i < v.NumField(); i++ {
			getValue := findFromMap(v.Type().Field(i).Name)
			if getValue != nil && reflect.ValueOf(getValue).Kind() == v.Field(i).Kind() {
				v.Field(i).Set(reflect.ValueOf(getValue))
			}
		}
	} else {
		panic("must be pointer")
	}
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

	x := &User{}
	m := map[string]interface{}{
		"Id":       123,
		"UserId":   101,
		"UserName": "yhkl",
		"age":      100,
	}
	Map2Struct(m, x)
	fmt.Println(x)
}
