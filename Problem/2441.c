/**
 * File : 2441.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2018 - 12 - 23
*/

#include <stdio.h>

int main(void)
{
	int i, j;
	int n;

	scanf("%d", &n);

	for (i = n; i > 0; i--)
	{
		for (j = i; j < n; j++)
		{
			printf(" ");
		}

		for (j = i; j > 0; j--)
		{
			printf("*");
		}

		printf("\n");
	}
	
	return 0;
}