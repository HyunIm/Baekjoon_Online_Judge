/**
 * File : 10872.c
 * Author : LimHyun (hyunzion@gmail.com)
 * Since : 2019 - 10 - 27
*/

#include <stdio.h>

int Factorial(int n);

int main(void)
{
	int n;

	scanf("%d", &n);

	printf("%d\n", Factorial(n));

	return 0;
}

int Factorial(int n)
{
	if (n <= 1)
	{
		return 1;
	}

	else
	{
		return n * Factorial(n - 1);
	}
}
