/**
 * File : 11022.c
 * Author : LimHyun (hyunzion@gmail.com)
 * Since : 2019 - 10 - 12
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

		printf("Case #%d: %d + %d = %d\n", i + 1, a, b, a + b);
	}

	return 0;
}
