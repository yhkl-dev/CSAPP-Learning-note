#include <stdio.h>
#include <stdlib.h>

#define OK 0
#define ERROR 1
#define Status int
#define ElementType int

typedef struct node {
	ElementType data;
	struct node *next;	
} Node;

Node* createLinkList(int length);
void printLinkList(Node *head);
int getLength(Node *head);
Status insertLinkList(Node *head, ElementType data, int position); 
Status deleteNode(Node *head, int position);


int main() {
	Node *head = createLinkList(5);
	printLinkList(head);
	insertLinkList(head, 100, 2);
	printLinkList(head);
	deleteNode(head, 2);
	printLinkList(head);
	return 0;

}


Node* createLinkList(int length) {
	Node *head;
	Node *tail = (Node *)malloc(sizeof(Node));
	head = tail;

	int i;
	for (i = 0; i < length; i++) {
		Node *node = (Node *)malloc(sizeof(Node));
		node->data = i;
		tail->next = node;
		tail = node;
	}
	return head;
}

void printLinkList(Node *head) {
	Node *cursor = head->next;
	
	printf("Single Link List: ");
	while (cursor != NULL) {
		printf("%d ", cursor->data);
		cursor = cursor->next;
	}
	printf("\n");
}

int getLength(Node *head) {
	Node *cursor = head->next;

	int i = 0;
	while (cursor != NULL) {
		cursor = cursor->next;
		i++;
	}
	return i;
}
Status insertLinkList(Node *head, ElementType data, int position) {
	Node *cursor = head->next;
	int i;

	if (position < 0 || position > getLength(head)) {
		return ERROR;
	}

	for (i = 0; i < position - 1; i++ ){
		cursor = cursor->next;
	}
	Node *node = (Node *)malloc(sizeof(Node));
	node->data = data;
	node->next = cursor->next;
	cursor->next = node;

	return OK;
}
Status deleteNode(Node *head, int position) {
	Node *cursor = head->next;
	int i;
	if (position < 0 || position > getLength(head)) {
		return ERROR;
	}

	for (i = 1; i < position; i++ ){
		cursor = cursor->next;
		printf("%d\n", cursor->data);
	}
	Node *deleted = cursor->next;
	printf("%d\n", deleted->data);
	if (deleted->next != NULL) {
		cursor->next = deleted->next;
	}
	free(deleted);
	return OK;
}
