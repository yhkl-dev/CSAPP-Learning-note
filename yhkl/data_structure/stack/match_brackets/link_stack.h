#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define ElementType char

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

