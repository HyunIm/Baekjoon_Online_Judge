/**
 * File : 2439.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2018 - 12 - 23
*/

#include <stdio.h>

int main(void)
{
	int i, j;
	int n;

	scanf("%d", &n);

	for (i = 0; i < n; i++)
	{
		for (j = n - 1; j > i; j--)
		{
			printf(" ");
		}

		for (j = 0; j < i + 1; j++)
		{
			printf("*");
		}
		printf("\n");
	}
	
	return 0;
}