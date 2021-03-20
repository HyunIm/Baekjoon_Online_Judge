/*
	* File : 1712.c
	* Dev : LimHyun (hyunzion@gmail.com)
	* Since : 2021-03-20
*/

#include <stdio.h>

int main(void)
{
	int A, B, C;
	int BEP = 0; // A + Bx < Cx

	scanf("%d %d %d", &A, &B, &C);

	if (B < C)
	{
		BEP = A / (C - B) + 1;
	}

	else
	{
		BEP = -1;
	}

	printf("%d", BEP);

	return 0;
}
