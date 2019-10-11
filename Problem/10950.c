/**
 * File : 10950.c
 * Author : LimHyun (hyunzion@gmail.com)
 * Since : 2019 - 10 - 11
*/

#include <stdio.h>

int main(void)
{
	int i;
	int t;
	int a, b;

	scanf("%d", &t);

	for (i = 0; i < t; i++)
	{
		scanf("%d %d", &a, &b);

		printf("%d\n", a + b);
	}

	return 0;
}
