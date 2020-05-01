#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define ElementType int

typedef struct StackNode {
	ElementType data;
	struct StackNode *next;
} stackNode, *linkStackPtr;

typedef struct LinkStack {
	stackNode *top;
	int count;
} linkStack; 

linkStack* initLinkStack();
void printStack(linkStack *l);
bool push(linkStack *l, ElementType data);
bool pop(linkStack *l, ElementType *e); 
bool isEmpty(linkStack *l);

int main() {
	linkStack *l = initLinkStack();
	printStack(l);

	push(l, 100);
	push(l, 200);
	printStack(l);
	
	ElementType data;
	pop(l, &data);
	printf("poped data: %d\n", data);
	return 0;
}

linkStack* initLinkStack() {
	linkStack *l = (linkStack *)malloc(sizeof(linkStack));
	l->count = 0;
	return l;
}

void printStack(linkStack *l) {
	if (l->count == 0) {
		printf("Empty Stack\n");
	}
	stackNode *s = l->top;
	
	while (s != NULL) {
		printf("%d ", s->data);
		s = s->next;
	}
	printf("\n");
}

bool push(linkStack *l, ElementType data) {
	linkStackPtr node = (linkStackPtr)malloc(sizeof(stackNode));

	node->data = data;
	node->next = l->top;
	l->top = node;
	l->count++;
	return true;
}

bool pop(linkStack *l, ElementType *e) {
	stackNode *cursor;
	if (isEmpty(l)) {
		return false;
	}
	*e = l->top->data;
	cursor = l->top;
	l->top = l->top->next;
	free(cursor);
	l->count--;
	return true;
}

bool isEmpty(linkStack *l) {
	if (l->count == 0 ) {
		return true;
	}
	return false;
}
