package limit

import (
	"fmt"
	"sync"
	"time"
)

// 限制携程数量
func job(index int) {
	time.Sleep(time.Millisecond * 500)
	fmt.Printf("exec done, num: %d\n", index)
}

var pool chan struct{}

func main() {
	fmt.Println("hello world")
	pool := make(chan struct{}, 10)
	wg := sync.WaitGroup{}
	for i := 0; i < 100; i++ {
		wg.Add(1)
		pool <- struct{}{} // 到达最大长度阻塞
		go func(index int) {
			defer wg.Done()
			defer func() {
				<-pool
			}()
			job(index)
		}(i)
	}
	wg.Wait()
}
