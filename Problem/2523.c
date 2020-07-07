/*
	* File : 2523.c
	* Dev : LimHyun (hyunzion@gmail.com)
	* Since : 2020-07-07
*/

#include <stdio.h>

int main(void)
{
	int i, j;
	int n;

	scanf("%d", &n);

	for (i = 0; i < n; i++)
	{
		for (j = 0; j < i + 1; j++)
			printf("*");
		printf("\n");
	}

	for (i = n - 1; i > 0; i--)
	{
		for (j = i; j > 0; j--)
		{
			printf("*");
		}
		printf("\n");
	}

	return 0;
}
