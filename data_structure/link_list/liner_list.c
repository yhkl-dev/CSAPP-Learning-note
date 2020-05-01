#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define ElementType int
#define LISTSIZE 10

typedef struct {
	ElementType data[LISTSIZE];
	int length;
} linerList;

linerList* initList(); 
void printList(linerList *L);
bool insertList(linerList *L, int position, ElementType data);
bool deleteList(linerList *L, int position, ElementType *e);


int main() {
	linerList *L = initList();	
	insertList(L, 1, 100);
	insertList(L, 1, 200);
	insertList(L, 1, 99);
	printList(L);
	ElementType data;
	deleteList(L, 2, &data);
	printf("deleted: %d\n", data);
	printList(L);
	return 0;
}

linerList* initList() {
	linerList *L = (linerList *)malloc(sizeof(linerList));
	L->length = 0;
	return L;
}

bool insertList(linerList *L, int position, ElementType data) {
	if (L->length == LISTSIZE) {
		return false;
	}
	if (position < 1 || position > L->length+1) {
		return false;
	}
	int k;
	if (position <= L->length) {
		for (k = L->length - position; k >= position - 1; k--) {
			L->data[k+1] = L->data[k];
		};
	}
	L->data[position-1] = data;
	L->length++;
	return true;

}

bool deleteList(linerList *L, int position, ElementType *e) {
	if (L->length == LISTSIZE) {
		return false;
	}
	if (position < 1 || position > L->length+1) {
		return false;
	}
	*e = L->data[position-1];
	int i;
	if (position < L->length) {
		for (i = position; i < L->length; i++) {
			L->data[i-1] = L->data[i];
		};
	}
	L->length--;
	return true; 
}

void printList(linerList *L) {
	if (L->length == 0) {
		printf("Empty List\n");
	}
	int i;
	printf("Liner List: ");
	for (i = 0; i< L->length; i++) {
		printf("%d ", L->data[i]);
	}
	printf("\n");
	return;
}
