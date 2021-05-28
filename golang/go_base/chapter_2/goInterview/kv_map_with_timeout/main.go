package main

import (
	"fmt"
	"sync"
	"time"
)

var kv sync.Map

func set(key string, value interface{}, expire time.Duration) {
	kv.Store(key, value)
	time.AfterFunc(expire, func() {
		kv.Delete(key)
	})
}

// 过期机制的map
func main() {
	set("id", 101, time.Second*5)
	set("name", "yhkl", time.Second*8)

	for {
		fmt.Println(kv.Load("id"))
		fmt.Println(kv.Load("name"))
		time.Sleep(time.Second)
	}

}
