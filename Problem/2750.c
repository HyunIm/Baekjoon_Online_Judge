/**
 * File : 2750.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 02 - 02
*/

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int i, j;
	int n;
	int tmp;
	int * arr;

	scanf("%d", &n);
	arr = (int *)malloc(sizeof(int) * n);

	for (i = 0; i < n; i++)
		scanf("%d", &arr[i]);

	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n - 1 - i; j++)
		{
			if (arr[j] > arr[j + 1])
			{
				tmp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = tmp;
			}
		}
	}

	for (i = 0; i < n; i++)
		printf("%d\n", arr[i]);

	return 0;
}
