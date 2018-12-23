/**
 * File : 8939.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2018 - 12 - 23
*/

#include <stdio.h>

int main(void)
{
	int i, n;
	int sum = 0;

	scanf("%d", &n);

	for (i = 1; i < n + 1; i++)
		sum += i;

	printf("%d\n", sum);

	return 0;
}