package String

import "fmt"

type String string

func (s String) Len() int {
	return len(s)
}

func NewString(str string) String {
	return String(str)
}

func FromInt(n int) String {
	return String(fmt.Sprintf("%d", n))
	//	return String(strconv.Itoa(n))
}
