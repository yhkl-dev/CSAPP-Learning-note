#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define ElementType int
#define QUEUESIZE 10

typedef struct {
	ElementType data[QUEUESIZE];
	int length;
} queue;

queue* initQueue() {
	queue *q = (queue*)malloc(sizeof(queue));
	q->length = 0;
	return q;
}

bool push(queue *q, ElementType e) {
	if (q->length == QUEUESIZE) {
		return false;
	}
	q->data[q->length] = e;
	q->length++;
	return true;
}

bool pop(queue *q, ElementType *e) {
	if (q->length == 0) {
		return false;
	}
	int i;
	*e = q->data[0];
	for (i = q->length-1; i> 0; i--) {
		q->data[i-1] = q->data[i];
	}
	q->length--;
	return true;
}

void printQueue(queue *q) {
	if (q->length == 0) {
		printf("Empty queue\n");
		return;
	}
	int i = 0;
	printf("Queue: ");
	for (i = 0; i < q->length; i++) {
		printf("%d ", q->data[i]);
	}

	printf("\n");
	return;
}

int main() {
	queue *q = initQueue();
	push(q, 1);
	push(q, 2);
	printQueue(q);
	ElementType data, data_1;
	pop(q, &data);
	pop(q, &data_1);
	printf("%d\n", data);
	printf("%d\n", data_1);
	printQueue(q);

	return 0;
}
