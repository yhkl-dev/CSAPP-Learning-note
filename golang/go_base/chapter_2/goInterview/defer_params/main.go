package main

import "fmt"

func show(i *int) {
	fmt.Println("show: ", *i)
}

// defer 定义函数时的参数问题
func main() {
	a := 1
	defer fmt.Println(a) // 在定义时确定了参数值
	defer func() {
		fmt.Println("defer function", a)
	}()
	defer func(input int) {
		fmt.Println("defer function input", input)
	}(a)
	defer show(&a)
	a++
}
