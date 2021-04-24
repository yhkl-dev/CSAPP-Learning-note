package String

import "fmt"

type String string

func (s String) Len() int {
	return len(s)
}

func (s String) Each(f func(item string)) {
	for _, c := range s {
		f(fmt.Sprintf("%c", c))
	}
}

func NewString(str string) String {
	return String(str)
}

func FromInt(n int) String {
	return String(fmt.Sprintf("%d", n))
	//	return String(strconv.Itoa(n))
}
