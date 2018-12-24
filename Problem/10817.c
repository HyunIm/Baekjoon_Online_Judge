/**
 * File : 10817.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2018 - 12 - 25
*/

#include <stdio.h>

int main(void)
{
	int i;
	int a, b, c;

	scanf("%d %d %d", &a, &b, &c);

	if (a > b)
	{
		if (a > c)
		{
			if (b > c)
				printf("%d\n", b);
			else
				printf("%d\n", c);
		}
		else
			printf("%d\n", a);
	}
	else	// a < b
	{
		if (a < c)
		{
			if (b < c)
				printf("%d\n", b);
			else
				printf("%d\n", c);
		}
		else
			printf("%d\n", a);
	}

	return 0;
}