/*
	* File : 14682.c
	* Dev : LimHyun (hyunzion@gmail.com)
	* Since : 2020-07-06
*/

#include <stdio.h>

int main(void)
{
	int x, y;

	scanf("%d", &x);
	scanf("%d", &y);

	if (x > 0 && y > 0)
		printf("1\n");
	else if (x < 0 && y > 0)
		printf("2\n");
	else if (x < 0 && y < 0)
		printf("3\n");
	else if (x > 0 && y < 0)
		printf("4\n");

	return 0;
}
