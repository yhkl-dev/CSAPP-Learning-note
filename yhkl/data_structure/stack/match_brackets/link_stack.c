#include "link_stack.h"

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


