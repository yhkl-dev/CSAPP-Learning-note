package main

import (
	"fmt"
	"sync"
)

// 如何精确处理共享内存
func main() {
	var wg sync.WaitGroup

	for i := 0; i < 10; i++ {
		wg.Add(1)
		go func(input int) {
			defer wg.Done()
			fmt.Println(input * 2)
		}(i)
	}
	wg.Wait()
	x()
}

func x() {
	c := make(chan int, 10)
	for i := 0; i < 10; i++ {
		go func(input int) {
			c <- input * 2
		}(i)
	}
	for i := 0; i < cap(c); i++ {
		fmt.Println(<-c)
	}
}
