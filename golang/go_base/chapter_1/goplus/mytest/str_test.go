package mytest

import (
	"goplus/src/Utils"
	"testing"
)

var strs = []string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"}

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

func BenchmarkJoin(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Utils.Join(strs...)
	}
}

func BenchmarkJoin2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Utils.Join2(strs...)
	}
}
func BenchmarkJoin3(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Utils.Join3(strs...)
	}
}
