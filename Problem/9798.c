/**
 * File : 9798.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2018 - 12 - 25
*/

#include <stdio.h>

int main(void)
{
	int n;

	scanf("%d", &n);

	if (n >= 90)
		printf("A\n");
	else if (n >= 80)
		printf("B\n");
	else if (n >= 70)
		printf("C\n");
	else if (n >= 60)
		printf("D\n");
	else
		printf("F\n");

	return 0;
}