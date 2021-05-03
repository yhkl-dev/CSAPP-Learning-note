package main

import "fmt"

/*
   逃逸分析
	GO在编译阶段确定内存使分配在栈还是堆上的一种行为

   知识点：
   	1.栈内存分配和释放非常快
	2.堆内存需要Go垃圾回收（占用CPU）
	3.通过逃逸分析，可以尽量把那些不要要分配到堆上的变量直接分配到栈上

   go的主要目的并不是希望程序员关注分配，而是通过编译时的代码分析自动决定

   局部变量原本应该在栈中分配，在栈中回收，由于返回时被外部引用，就会逃逸

   参数为interface类型时，比如fmt.Println(a ...interface{}) 编译时很难确定其参数的具体类型，所以也会产生逃逸

   自定义strct时需要注意是否是指针
*/

func test() []int {
	a := []int{1, 2, 3}
	a[1] = 4
	fmt.Println(a)
	return a
}

func main() {
	// go build -gcflags=-m main.go
	test()

}
