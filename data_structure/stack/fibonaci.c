#include <stdio.h>

int fib_iter(int a, int b, int count );
int fib(int n); 
int main() {
	int res =  fib(4);
	printf("%d\n", res);
	return 0;
}
int fib(int n) {
	int i = fib_iter(1, 0, n);
	return i;
}

int fib_iter(int a, int b, int count ) {
	if (count == 0) {
		return b;
	}
	fib_iter(a+b, a, count-1);
}



