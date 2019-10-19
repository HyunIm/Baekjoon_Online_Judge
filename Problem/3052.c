/**
 * File : 3052.c
 * Author : LimHyun (hyunzion@gmail.com)
 * Since : 2019 - 10 - 19
*/

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int i;
	int n;
	int count = 0;
	int *arr;
	int cnt[42];
	
	n = 10;
	arr = (int *)malloc(sizeof(int) * n);

	for (i = 0; i < n; i++)
		scanf("%d", &arr[i]);
	for (i = 0; i < 42; i++)
		cnt[i] = 0;

	for (i = 0; i < n; i++)
	{
		cnt[arr[i] % 42]++;
	}

	for (i = 0; i < 42; i++)
	{
		if (cnt[i] > 0)
			count++;
	}

	printf("%d\n", count);

	free(arr);

	return 0;
}
