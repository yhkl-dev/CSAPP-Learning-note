#include <stdio.h>
#include <stdlib.h>

#define OK 0
#define ERROR 1
#define ElementType int
#define Status int
#define MAXSIZE 1000

typedef struct Component {
	ElementType data;
	int cursor;
} StaticLinkList[MAXSIZE];

Status initStaticLinkList();


int main() {
	StaticLinkList L;
	initStaticLinkList(L);	
	return 0;
}

Status initStaticLinkList(StaticLinkList L) {
	int i;
	for (i = 0; i < MAXSIZE -1; i++) {
		L[i].cursor = i+1;
	}
	L[MAXSIZE-1].cursor = 0;
	return OK;
}

int mallocSLL(StaticLinkList L) {
	int i = L[0].cursor;
	if (L[0].cursor) {
		L[0].cursor = L[i].cursor;
	}
	return i;
}

int getListLength(StaticLinkList L) {
	int i = L[MAXSIZE-1].cursor;
	int j = 0;
	while (L[i].data) {
		i = L[i].cursor;
		j++;
	}
	return j;
}

Status insertList(StaticLinkList L, int i, ElementType e) {
	int j, k , l;
	k = MAXSIZE - 1;
	if (i < 1 || i > getListLength(L) + 1) {
		return ERROR;
	}
	j = mallocSLL(L);
	if (j) {
		L[j].data = e;
		for (l = 1; l <= i - 1; l++) {
			k = L[k].cursor;
		}
		L[j].cursor = L[k].cursor;
		L[k].cursor = j;
		return OK;
	}
	return ERROR;
}

void freeSLL(StaticLinkList L, int k) {
	L[k].cursor = L[0].cursor;
	L[0].cursor = k;
}

Status deleteList(StaticLinkList L, int i) {
	int j, k;
	if (i < 1 || i > getListLength(L)) {
		return ERROR;
	}
	k = MAXSIZE - 1;
	for (j = 1; j <= i - 1; j++ ){
		k = L[k].cursor;
	}
	j = L[k].cursor;
	L[k].cursor = L[j].cursor;
	freeSLL(L, j);
	return OK;
}

