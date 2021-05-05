package main

import (
	"fmt"
	"sync"
	"time"
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

	/*
		x := make(chan int, 3)

			r := make(chan struct{})
			go producer(x)
			go consumer(x, r)
			<-r
	*/
	x := make(chan int, 3)
	go producer(x)
	r := consumer2(x)
	<-r
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

func producer(out chan int) {
	defer close(out)
	for i := 0; i < 5; i++ {
		out <- i * 2
		time.Sleep(time.Second * 2)
	}
}

func consumer(out chan int, r chan struct{}) {
	for item := range out {
		fmt.Println(item)
	}
	r <- struct{}{}
}
func consumer2(out chan int) (r chan struct{}) {
	r = make(chan struct{})
	go func() {
		defer func() {
			r <- struct{}{}
		}()
		for item := range out {
			fmt.Println(item)
		}
	}()
	return r
}
