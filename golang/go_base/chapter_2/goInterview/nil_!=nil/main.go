package main

import (
	"fmt"
	"reflect"
)

// nil != nil ?
// interface 包含两个属性， 类型和值，必须两个都是nil才行
func main() {
	var f func()
	var a *struct{}
	listA := []interface{}{f, a}
	for _, item := range listA {
		if reflect.ValueOf(item).IsNil() {
			fmt.Println("nil")
		}
		// if item == nil {
		// 	fmt.Println("nil")
		// }
		// if item != nil {
		// 	fmt.Println("not nil")
		// }
		// if v, ok := item.(func()); ok && v == nil {
		// 	fmt.Println("nil func")
		// }
		// if v, ok := item.(*struct{}); ok && v == nil {
		// 	fmt.Println("nil struct")
		// }
	}
}
