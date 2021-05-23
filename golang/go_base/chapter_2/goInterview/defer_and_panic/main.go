package main

import "fmt"

// defer和panic哪个先执行
// func main() {
// 	defer func() {
// 		fmt.Println("before print")
// 	}()
// 	defer func() {
// 		fmt.Println("on printing")
// 	}()
// 	defer func() {
// 		fmt.Println("after print")
// 	}()
// 	panic("Exception")
// }

func main() {
	func() {
		defer func() {
			fmt.Println("before print")
		}()
		defer func() {
			fmt.Println("on printing")
		}()
		defer func() {
			fmt.Println("after print")
		}()
		panic("Exception")
	}()
	panic("Exception2")
}
