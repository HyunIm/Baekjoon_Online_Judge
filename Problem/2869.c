/*
	* File : 2869.c
	* Dev : LimHyun (hyunzion@gmail.com)
	* Since : 2021-05-01
*/

#include <stdio.h>
#include <math.h>

int main(void)
{
	int A, B, V;
	int day = 0;

	scanf("%d %d %d", &A, &B, &V);

	day = ceil((double)(V - B) / (A - B));

	printf("%d\n", day);

	return 0;
}
