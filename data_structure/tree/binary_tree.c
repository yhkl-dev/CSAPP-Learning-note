#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define ElementType int
#define TElementType char

typedef struct Node {
	ElementType data;
	struct Node *left;
	struct Node *right;
} treeNode, *Tree;

treeNode* createTree();
void traverseTree(treeNode *root);
void preTraverseTree(treeNode *root);
void midTraverseTree(treeNode *root);
void lastTraverseTree(treeNode *root);
void createBiTree(Tree *node);

int main() {
	Tree *n = (Tree*)malloc(sizeof(Tree));
	createBiTree(n);
	preTraverseTree(*n);

	treeNode *root = createTree();
	printf("pre\n");
	preTraverseTree(root);
	printf("mid\n");
	midTraverseTree(root);
	printf("list\n");
	lastTraverseTree(root);
	
	return 0;
}


treeNode* createTree() {
	treeNode *node = (treeNode *)malloc(sizeof(treeNode));
	treeNode *node_1 = (treeNode *)malloc(sizeof(treeNode));
	treeNode *node_2 = (treeNode *)malloc(sizeof(treeNode));
	treeNode *node_3 = (treeNode *)malloc(sizeof(treeNode));
	treeNode *node_4 = (treeNode *)malloc(sizeof(treeNode));
	node->data = 1;
	node->left = node_1;
	node->right = node_2;
	node_1->data = 2;
	node_2->data = 3;
	node_3->data = 4;
	node_4->data = 5;

	node_1->left = node_3;
	node_1->right = node_4;
	return node;
}

void preTraverseTree(treeNode *root) {
	if (!root) {
		return;
	}
	printf("%d\n", root->data);
	preTraverseTree(root->left);
	preTraverseTree(root->right);
}

void midTraverseTree(treeNode *root) {
	if (!root) {
		return;
	}
	midTraverseTree(root->left);
	printf("%d\n", root->data);
	midTraverseTree(root->right);
}

void lastTraverseTree(treeNode *root) {
	if (!root) {
		return;
	}
	printf("%d\n", root->data);
	lastTraverseTree(root->right);
	lastTraverseTree(root->left);
}

void createBiTree(Tree *node) {
	TElementType data;
	scanf("%c", &data);
	if (data == '#') {
		*node = NULL;
	} else {
		*node = (treeNode *)malloc(sizeof(treeNode));
		if (!node) {
			exit(-1);
		}
		(*node)->data = data;
		createBiTree(&(*node)->left);
		createBiTree(&(*node)->right);
	}
}
