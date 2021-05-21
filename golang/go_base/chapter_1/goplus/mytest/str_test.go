package mytest

import (
	"goplus/src/Utils"
	"testing"
)

func TestStr(t *testing.T) {
	str := Utils.Join("abc", "bcd", "xyz")
	t.Log(str)
}
func TestJoin(t *testing.T) {
	type args struct {
		strs []string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{name: "t1", args: args{[]string{"a", "b"}}, want: "ab"},
		{name: "t1", args: args{[]string{"a", "b", "c"}}, want: "abc"},
		{name: "t1", args: args{[]string{"a", "b", "c", "d"}}, want: "abcd"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Utils.Join(tt.args.strs...); got != tt.want {
				t.Errorf("Join() = %v, want %v", got, tt.want)
			}
		})
	}
}
