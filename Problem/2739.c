/**
 * File : 2739.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2018 - 12 - 23
*/

#include <stdio.h>

int main(void)
{
	int i;
	int n;

	scanf("%d", &n);

	for (i = 1; i < 10; i++)
	{
		printf("%d * %d = %d\n", n, i, n * i);
	}
	
	return 0;
}