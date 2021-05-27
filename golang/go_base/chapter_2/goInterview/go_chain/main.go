package main

import (
	"container/list"
	"fmt"
)

func main() {
	fmt.Println("vim-go")
	data := list.New()
	x := data.PushBack(8)
	data.PushBack(8)
	data.PushBack(9)
	data.PushBack(10)

	data.PushFront(100)
	x1 := data.InsertAfter(101, x)
	data.MoveAfter(x1, x)
	for e := data.Front(); e != nil; e = e.Next() {
		fmt.Printf(" %v", e.Value)
	}
}
