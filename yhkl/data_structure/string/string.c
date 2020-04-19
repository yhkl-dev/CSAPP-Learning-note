#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool stringAssign(char t[], char *chars);
int stringLength(char *chars);

int main() {

	char x[] = "hello world";
	printf("length %d\n", stringLength(x));

	char *new_x;
	
	stringAssign("hello world new", new_x);	
	printf("%s\n", new_x);

	return 0;
}

bool stringAssign(char *t, char *chars) {
	printf("common string %s\n", t);
	printf("\n");
//	printf("string length for assign %d\n", stringLength(t));

	strcpy(t, chars);
		
	return true;
}

int stringLength(char *chars) {
	int length = 0;
	while (chars[length] != '\0') {
		chars[length] = chars[length+1];
		length++;
	}
	return length;
}
