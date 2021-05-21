package Utils

func Join(strs ...string) string {
	ret := ""
	for _, s := range strs {
		ret += s
	}
	return ret
}
