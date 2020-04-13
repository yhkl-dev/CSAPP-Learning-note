#include <stdio.h>
#include <stdbool.h>
#include "link_stack.h"
#include <string.h>


int match(char *match_data);


int main() {
	char match_data[] = "()()()[]]";
	
	int value = match(match_data);
	printf("%d\n", value);
	if (value == 1) {
		printf("true\n");
	} else {
		printf("false\n");
	}
	

	return 0;
}


int match(char *match_data) {
	
	int i;
	linkStack *s = initLinkStack();

	for (i = 0; i < strlen(match_data); i++) {
		char x[2];
		x[0] = match_data[i];
		x[1] = '\0';
		if (strcmp(x, "(") == 0 || strcmp(x, "[") == 0 || strcmp(x, "{") == 0) {
			push(s, x);
		}
		if (strcmp(x, ")") == 0 || strcmp(x, "]") == 0 || strcmp(x, "}") == 0) {
			ElementType y[2];
			pop(s, y);
		}
	}
	if (isEmpty(s)) {
		return 0;
	}
	return 1;
}
