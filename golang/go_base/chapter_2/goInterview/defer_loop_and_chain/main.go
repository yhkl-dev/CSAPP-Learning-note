package main

import "fmt"

/*
	defer 使用链式调用，循环等
*/
type test struct{}

func NewTest() *test {
	return &test{}
}

func (t *test) do(i int) *test {
	fmt.Println(i)
	return t
}

func main() {
	// 链式调用
	t := NewTest()
	t.do(1).do(2)
	defer func() {
		t.do(101).do(102).do(103)
	}()
	defer t.do(4).do(5).do(100) // 只有最后一个延迟执行
	t.do(3)
	fmt.Println("____________")
	for i := 0; i < 3; i++ {
		defer fmt.Println(i)
		defer func() {
			fmt.Println(i)
		}()
	}
}
