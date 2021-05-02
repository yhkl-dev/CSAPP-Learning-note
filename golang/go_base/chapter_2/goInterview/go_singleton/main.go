package main

import (
	"fmt"
	"sync"
)

type WebConfig struct {
	Port int
}

var cc *WebConfig

var mu sync.Mutex

func GetConfig() *WebConfig {
	mu.Lock()
	defer mu.Unlock()
	if cc == nil {
		cc = &WebConfig{Port: 8000}
	}
	return cc
}

var once sync.Once

func GetConfig2() *WebConfig {
	once.Do(func() {
		cc = &WebConfig{Port: 8080}
	})
	return cc
}

func main() {

	c := GetConfig()
	c2 := GetConfig()
	c3 := GetConfig()
	c3.Port = 9000

	fmt.Println(c == c2, c2 == c3)
	fmt.Println(c)
}
