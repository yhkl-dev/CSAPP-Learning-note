package Utils

import (
	"bytes"
	"strings"
)

func Join(strs ...string) string {
	ret := ""
	for _, s := range strs {
		ret += s
	}
	return ret
}

func Join2(strs ...string) string {
	return strings.Join(strs, "")
}

func Join3(strs ...string) string {
	var by bytes.Buffer
	for _, s := range strs {
		by.WriteString(s)
	}
	return by.String()
}
