#include <stdio.h>

void printArray(int *array, int length) {
	int i;
	for (i = 0; i < length; i++ ){
		printf("%d\n", array[i]);
	};

}

int main() {
	int array[] = {8, 4, 2, 9, 3, 6};
	int pos, cursor;
	int i;
	int length = sizeof(array)/(sizeof(array[0]));
	
	printArray(array, length);
	for (i = 1; i < length; i++ ){
		pos = i - 1;
		cursor = array[i];
		while (pos >=0 && array[pos] > cursor) {
			array[pos + 1] = array[pos];
			pos--;
		}
		array[pos + 1] = cursor;
	}
	printf("After:\n");;
	printArray(array, length);

	return 0;
}

