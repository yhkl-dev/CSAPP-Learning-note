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
void printStack(sharedStack *s, int stackNumber);
bool push(sharedStack *s, ElementType data, int stackNumber);
bool pop(sharedStack *s, ElementType *e, int stackNumber);

int main() {
	sharedStack *s = initStack();
	push(s, 100, 1);
	push(s, 1001, 1);
	push(s, 999, 1);
	
	printStack(s, 1);
	
	push(s, 2, 2);
	push(s, 200, 2);
	printStack(s, 2);
	
	ElementType data;
	pop(s, &data, 1);
	printf("%d\n", data);
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
		s->top_1++;
		s->data[s->top_1] = data;
	} else if (stackNumber == 2) {
		s->top_2--;
		s->data[s->top_2] = data;
	} else {
		return false;
	}
	
	return true;
}

void printStack(sharedStack *s, int stackNumber) {
	int i;
	if (s->top_1 == -1 && s->top_2 == STACKSIZE) {
		printf("Empty Stack \n");
		return;
	}
	printf("SharedStack Stacknumber: %d, data: ", stackNumber);
	if (stackNumber == 1) {
		for (i = 0; i <= s->top_1; i++) {
			printf("%d ", s->data[i]);
		}
		printf("\n");
	} else if (stackNumber == 2) {
		for (i = STACKSIZE-1; i >= s->top_2; i--) {
			printf("%d ", s->data[i]);
		}
		printf("\n");

	} else {
		printf("Wrong stackNumber \n");
	}
	return;
}

bool pop(sharedStack *s, ElementType *e, int stackNumber) {
	if (s->top_1 == -1 ) {
		printf("Empty Stack \n");
		return false;
	}
	if (s->top_2 == STACKSIZE) { 
		printf("Empty Stack \n");
		return false;
	}
	if (stackNumber == 1 ) {
		*e = s->data[s->top_1];
		s->top_1--;
	} else if (stackNumber == 2) {
		*e = s->data[s->top_2];
		s->top_2++;
	} else {
		return false;
	}
	return true;
}
