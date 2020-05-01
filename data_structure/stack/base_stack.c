#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define OK 0
#define ERROR 1
#define Status int
#define ElementType int
#define STACKSIZE 5

typedef struct Stack {
	ElementType data[STACKSIZE];
	int top;
} stack;

stack* initStack(); 
Status push(stack *s, ElementType data);
Status pop(stack *s, ElementType *e);
void printStackData(stack *s);
bool isEmpty(stack *s);
Status clearStack(stack *s); 
Status DestroyStack(stack *s); 

int main() {
	stack *s = initStack();
	push(s, 100);
	push(s, 101);
	push(s, 1021);
	printStackData(s);
	
	ElementType e;
	pop(s, &e);
	printf("poped data: %d\n", e);
	printStackData(s);
	return 0;
}


stack* initStack() {
	stack *CStack = (stack *)malloc(sizeof(stack));	
	CStack->top = -1;
	return CStack; 
}

Status push(stack *s, ElementType data) {
	if (s->top <= STACKSIZE - 1) {
		s->top++;
		s->data[s->top] = data;
		return OK;
	}
	return ERROR;
}

Status pop(stack *s, ElementType *e) {
	if (s->top != -1) {
		printf("top: %d\n", s->top);
		*e = s->data[s->top];
		s->top--;
		return OK;
	}
	return ERROR;
}

void printStackData(stack *s) {
	int i;
	printf("Stack data: ");
	for (i = 0; i <= s->top; i++) {
		printf("%d ", s->data[i]);
	}
	printf("\n");
}

bool isEmpty(stack *s) {
	if (s->top == -1) {
		return true;
	}
	return false;
}

Status clearStack(stack *s) {
	s->top = -1;
	return OK;
}

Status DestroyStack(stack *s) {
	free(s);
	return OK;
}
