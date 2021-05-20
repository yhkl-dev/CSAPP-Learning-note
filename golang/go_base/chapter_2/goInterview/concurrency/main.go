package main

import (
	"fmt"
	"sync"
)

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
}
