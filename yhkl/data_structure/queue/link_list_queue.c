#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define ElementType int

typedef struct QueueNode {
	ElementType data;
	struct QueueNode *next;
} node, queue;

queue* initQueue();
bool push(queue *q, ElementType value);
bool pop(queue *q, ElementType *e);

int main() {
	return 0;
}
