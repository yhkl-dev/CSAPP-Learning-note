#include <stdio.h>
#include <stdbool.h>
#include "link_stack.h"

bool match(char *data);


int main() {
	printf("hello world\n");

	char match_data[] = "()()()";
	
	linkStack *l = initLinkStack();
	printStack(l);

	char a = '1';
	push(l, a);
	printStack(l);
	
	ElementType data;
	pop(l, &data);
	printf("poped data: %d\n", data);
	printf("--------------\n");
	match(match_data);	

	return 0;
}

bool match(char *data) {
	printf("%s\n", data);
	return false;
}
