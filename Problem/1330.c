/**
 * File : 1330.c
 * Author : LimHyun (hyunzion@gmail.com)
 * Since : 2019 - 10 - 07
*/

#include <stdio.h>

int main(void)
{
	int A, B;

	scanf("%d", &A);
	scanf("%d", &B);

	if (A > B)
		printf(">\n");
	else if (A < B)
		printf("<\n");
	else if (A == B)
		printf("==\n");

	return 0;
}
