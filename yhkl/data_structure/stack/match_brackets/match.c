#include <stdio.h>
#include <stdbool.h>
#include "link_stack.h"
#include <string.h>


bool match(char *data);


int main() {
	printf("hello world\n");

	char match_data[] = "()()()";
	
	printf("--------------\n");
	match(match_data);	

	return 0;
}

bool match(char *data) {
	
	int len = strlen(data);
	int i;
	for (i = 0; i < len; i++) {
		printf("%c\n", data[i]);
	}

	printf("\n");
	return false;
}
