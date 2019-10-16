/**
 * File : 10818.c
 * Author : LimHyun (hyunzion@gmail.com)
 * Since : 2019 - 10 - 16
*/

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int i;
	int n;
	int max, min;
	int *arr;
	
	scanf("%d", &n);
	arr = (int *)malloc(sizeof(int) * n);

	for (i = 0; i < n; i++)
		scanf("%d", &arr[i]);

	max = arr[0];
	min = arr[0];
	for (i = 0; i < n; i++)
	{
		if (max < arr[i])
			max = arr[i];
		if (min > arr[i])
			min = arr[i];
	}

	printf("%d %d", min, max);

	return 0;
}
