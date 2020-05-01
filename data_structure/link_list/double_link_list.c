#include <stdio.h>
#include <stdlib.h>

#define OK 0
#define ERROR 1
#define Status int
#define ElementType int

typedef struct node {
	ElementType data;
	struct node *next;
	struct node *prev;
} node; 

node* createDoubleLinkList(int length);
void printDoublelLinkList(node *head);
void printByReverse(node *head);
Status insertNode(node *head, int position, ElementType data);
Status deleteNode(node *head, int position);


int main() {
	node *head = createDoubleLinkList(5);
	printDoublelLinkList(head);
	printByReverse(head);

	insertNode(head, 3, 100);
	printDoublelLinkList(head);
	printByReverse(head);

	deleteNode(head, 1);
	printDoublelLinkList(head);
	printByReverse(head);

	return 0;
}

node* createDoubleLinkList(int length) {
	node *head;
	node *tail = (node *)malloc(sizeof(node));
	head = tail;
	head->next = head->prev = tail;
	
	int i;
	for (i = 0; i < length; i++) {
		node *element = (node*)malloc(sizeof(node));
		element->data = i;
		tail->next = element;
		element->prev = tail;
		tail = element;
	}
	head->prev = tail;
	tail->next = head;
	return head;
}

void printDoublelLinkList(node *head) {
	node *cursor = head->next;
	printf("Double Linked List: ");
	while (cursor != head) {
		printf("%d ", cursor->data);
		cursor = cursor->next;
	}
	printf("\n");
}

void printByReverse(node *head) {
	node *cursor = head->prev;
	printf("Double Linked List: ");
	while (cursor != head) {
		printf("%d ", cursor->data);
		cursor = cursor->prev;
	}
	printf("\n");

}

int getDoubleLinkListLength(node *head) {
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
	if ( position < 0 || position > getDoubleLinkListLength(head)) {
		return ERROR;
	} 
	// locate node
	int i;
	for (i = 1; i <= position -1; i++) {
		cursor = cursor->next;
	}
	node *element = (node*)malloc(sizeof(node));
	element->data = data;
	element->next = cursor->next;
	cursor->next->prev = element;
	element->prev = cursor;
	cursor->next = element;
	return OK;
}

Status deleteNode(node *head, int position) {
	node *cursor = head;
	if (position < 0 || position > getDoubleLinkListLength(head)) {
		return ERROR;
	}
	int i;
	printf("%d\n", position);
	printf("cursor data: %d\n", cursor->data);
	for (i = 0; i < position - 1; i++) {
		cursor = cursor->next;
	}

	node *deleted = cursor->next;
	cursor->next = deleted->next;
	deleted->next->prev = cursor;
	free(deleted);

	return OK;
}
