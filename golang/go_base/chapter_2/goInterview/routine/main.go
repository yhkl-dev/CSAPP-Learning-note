package main

import (
	"fmt"
	"runtime"
	"sync"
)

// 协程为什么总是先输出倒数第一个
// 默认情况下，go使用所有得cpu核，
// 单核情况下，所有goroutine运行在同一个线程M中，线程维护一个上下文P
// 程序中，我们运行了若干协程，而且是单核
// 1.P就绪后，开始执行，默认先执行的是最后一个创建的协程
// 2.然后再继续执行其他协程，此次是按顺序来的
func main() {
	runtime.GOMAXPROCS(1)
	wg := sync.WaitGroup{}
	wg.Add(6)
	for i := 0; i < 5; i++ {
		go func(i int) {
			defer wg.Done()
			fmt.Printf("%d", i)
		}(i)
	}
	go func() {
		defer wg.Done()

		fmt.Println("start run")
	}()
	wg.Wait()
}
