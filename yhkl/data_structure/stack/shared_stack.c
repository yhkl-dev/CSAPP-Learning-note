#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define STACKSIZE 5
#define ElementType int

typedef struct SharedStack {
	ElementType data[STACKSIZE];
	int top_1;
	int top_2;
} sharedStack;

sharedStack* initStack();
bool push(sharedStack *s, ElementType data, int stackNumber);

int main() {

	return 0;
}

sharedStack* initStack() {
	sharedStack *s = (sharedStack *)malloc(sizeof(sharedStack));
	s->top_1 = -1;
	s->top_2 = STACKSIZE;
	return s;
}
bool push(sharedStack *s, ElementType data, int stackNumber) {
	if (s->top_1 + 1 == s->top_2) {
		printf("Stack has been full\n");
		return false;
	}

	if (stackNumber == 1) {

		
	}
	return true;
}
