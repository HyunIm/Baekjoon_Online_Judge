/**
 * File : 1110.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2018 - 12 - 30
*/

#include <stdio.h>

int main(void)
{
	int n, old_n;
	int a, b, c;
	int count = 1;

	scanf("%d", &n);

	old_n = n;

	while (1)
	{
		a = n / 10;
		b = n % 10;

		c = a + b;
		c %= 10;

		n = (b * 10) + c;

		if (old_n == n)
			break;

		count++;
	}

	printf("%d\n", count);

	return 0;
}
