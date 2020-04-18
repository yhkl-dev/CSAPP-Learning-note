#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define ElementType int

typedef struct QueueNode {
	ElementType data;
	struct QueueNode *next;
} node;

typedef struct {
	node *head;
	node *tail;
} queue;

queue* initQueue();
bool push(queue *q, ElementType value);
bool pop(queue *q, ElementType *e);
void printQueue(queue *q);

int main() {
	queue *q = initQueue();
	printf("push\n");	
	push(q, 100);
	push(q, 200);
	printQueue(q);
	
	printf("poped\n");
	ElementType data;
	pop(q, &data);
	printQueue(q); 
	printf("poped: %d\n", data);

	return 0;
}

queue* initQueue() {
	queue *q = (queue *)malloc(sizeof(queue));
	q->head = q->tail = (node*)malloc(sizeof(node));
	return q;
}


bool push(queue *q, ElementType value) {
	node *element = (node *)malloc(sizeof(node));
	element->data = value;
	element->next = NULL;
	q->tail->next = element;
	q->tail = element;
	return true;
}

bool pop(queue *q, ElementType *e) {
	node *element = q->head->next;
	*e = element->data;
	q->head->next = element->next;
	free(element);
	return true;
}

void printQueue(queue *q) {
	node *element = q->head->next;;

	while (element != NULL) {
		printf("%d ", element->data);
		element = element->next;
	}
	printf("\n");
	return;
}
