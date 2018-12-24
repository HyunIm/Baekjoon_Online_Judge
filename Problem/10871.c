/**
 * File : 10871.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2018 - 12 - 25
*/

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int i;
	int n, x;
	int *arr;

	scanf("%d %d", &n, &x);

	arr = malloc(sizeof(int) * n);

	for (i = 0; i < n; i++)
	{
		scanf("%d", &arr[i]);

		if (arr[i] < x)
			printf("%d ", arr[i]);
	}

	free(arr);

	return 0;
}