#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define VertexType char
#define EdgeType int
#define MAXVEX 100
#define INFINITY 65535

typedef struct {
	VertexType vexs[MAXVEX];
	EdgeType arc[MAXVEX][MAXVEX];
	int numVertexes, numEdges;
} MGraph;

void createMGraph(MGraph *G) {
	int i, j, k, w;
	printf("输入顶点和边数: \n");
	scanf("%d, %d", &G->numVertexes, &G->numEdges);

	for (i = 0; i < G->numVertexes; i++) {
		scanf(&G->vexs[i]);
	}

	for (i = 0; i < G->numVertexes; i++) {
		for (j = 0; j < G->numVertexes; j++) {
			G->arc[i][j];
		}
	}
	for (k = 0; k< G->numEdges; k++) {
		printf("输入边（vi， vj）上的下标i， 下标j和权w");
		scanf("%d, %d, %d", &i, &j, &w);
		G->arc[i][j] = w;
		G->arc[j][i] = G->arc[i][j];
	}
}
