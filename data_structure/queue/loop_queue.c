#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define ElementType int
#define QUEUESIZE 5

typedef struct {
	ElementType data[QUEUESIZE];
	int head;
	int rear;
} loopQueue;

loopQueue* initQueue();
bool push(loopQueue *q, ElementType data);
bool pop(loopQueue *q, ElementType *e); 
void printQueue(loopQueue *q);

int main() {
	loopQueue *q = initQueue();
	push(q, 100);
	push(q, 100);
	push(q, 100);
	push(q, 100);
	ElementType data_1;
	ElementType data_2;
	pop(q, &data_1);
	pop(q, &data_2);

	printQueue(q);
	push(q, 200);
	push(q, 200);
	printQueue(q);
	return 0;
}


loopQueue* initQueue() {
	loopQueue *q = (loopQueue*)malloc(sizeof(loopQueue));
	q->head = 0;
	q->rear = 0;
	return q;
}


bool push(loopQueue *q, ElementType data) {
	if ((q->rear+1) % QUEUESIZE == q->head) {
		return false;
	}
	q->data[q->rear] = data;
	q->rear = (q->rear+1) % QUEUESIZE;
	
	return true;
}

bool pop(loopQueue *q, ElementType *e) {
	if (q->rear == q->head) {
		return false;
	}
	*e = q->data[q->head];
	q->head = (q->head+1);
	return true;
}

int queueLength(loopQueue *q) {
	return (q->rear - q->head + QUEUESIZE) % QUEUESIZE;
}

void printQueue(loopQueue *q) {
	if (q->head == q->rear) {
		printf("Empty queue\n");
	}	
	printf("Loop Queue: ");
	int i;
	if (q->head < q->rear) {
		for (i = q->head; i < q->rear; i++) {
			printf("%d ", q->data[i]);
		}
	}
	if (q->head > q->rear) {
		for (i = q->head; i < QUEUESIZE; i++) {
			printf("%d ", q->data[i]);
		};	
		for (i = 0; i < q->rear; i++) {
			printf("%d ", q->data[i]);
		};
	}
	printf("\n");
	return;
}
