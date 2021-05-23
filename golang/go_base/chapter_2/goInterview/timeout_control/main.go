package main

import (
	"fmt"
	"time"
)

// title 超时控制函数
// 1.业务过程放到携程
// 2.把业务结果塞到channel
func job() chan string {
	ret := make(chan string)
	go func() {
		time.Sleep(time.Second * 2)
		ret <- "success"
	}()
	return ret
}

func run() (interface{}, error) {
	c := job()
	select {
	case r := <-c:
		return r, nil
	case <-time.After(time.Second * 3):
		return nil, fmt.Errorf("timeout")
	}
}

func main() {
	fmt.Println(run())
}
