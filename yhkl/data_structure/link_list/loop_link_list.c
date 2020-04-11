#include <stdio.h>
#include <stdlib.h>

#define OK 0
#define ERROR 1
#define Status int
#define ElementType int

typedef struct Node {
	ElementType data;
	struct Node *next;
} node;

node* createLoopLinkList(int length); 
void printLoopLinkList(node *head);
int getLinkListLength(node *head);
Status insertNode(node *head, int position, ElementType data); 
Status deleteNode(node *head, int position);

int main() {
	node *head = createLoopLinkList(5);	
	printLoopLinkList(head);
	printf("list length: %d\n", getLinkListLength(head));
	insertNode(head, 3, 100);
	printLoopLinkList(head);
	printf("list length: %d\n", getLinkListLength(head));

	deleteNode(head, 4);
	printLoopLinkList(head);
	printf("list length: %d\n", getLinkListLength(head));
	return 0;
}

node* createLoopLinkList(int length) {
	node *head;
	node *tail = (node *)malloc(sizeof(node));
	head = tail;
	int i;
	for (i = 0; i < length; i++) {
		node *element = (node *)malloc(sizeof(node));
		element->data = i;
		tail->next = element;
		tail = element;
	}
	tail->next = head;
	return head;
}
void printLoopLinkList(node *head) {
	node *cursor = head->next;
	
	printf("Loop Link List: ");
	while (cursor != head) {
		printf("%d ", cursor->data);
		cursor = cursor->next;
	}
	printf("\n");
}

int getLinkListLength(node *head) {
	node *cursor = head->next;
	int i = 0;
	while (cursor != head) {
		cursor = cursor->next;
		i++;
	}
	return i;
}

Status insertNode(node *head, int position, ElementType data) {
	node *cursor = head->next;

	if (position < 0 || position > getLinkListLength(head)) {
		return ERROR;
	}
	int i;
	for (i = 1; i <= position - 1; i++ ) {
		cursor = cursor->next;
	}

	node *new_node = (node*)malloc(sizeof(node));
	new_node->data = data;
	new_node->next = cursor->next;
	cursor->next = new_node;
	return OK;
}

Status deleteNode(node *head, int position) {
	node *cursor = head->next;
	
	if (position < 0 || position > getLinkListLength(head)) {
		return ERROR;
	}

	int i;
	for (i = 1; i <= position - 1; i++ ) {
		cursor = cursor->next;
	}
	node *deleted = cursor->next;
	cursor->next = deleted->next;
	free(deleted);
	return OK;
}
