/**
 * File : 2562.c
 * Author : LimHyun (hyunzion@gmail.com)
 * Since : 2019 - 10 - 17
*/

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int i;
	int n;
	int max;
	int max_i = 0;
	int *arr;
	
	n = 9;
	arr = (int *)malloc(sizeof(int) * n);

	for (i = 0; i < n; i++)
		scanf("%d", &arr[i]);

	max = arr[0];
	for (i = 0; i < n; i++)
	{
		if (max < arr[i])
		{
			max = arr[i];
			max_i = i;
		}
	}

	printf("%d %d\n", max, max_i + 1);

	free(arr);

	return 0;
}
