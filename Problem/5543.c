/*
	* File : 5543.c
	* Dev : LimHyun (hyunzion@gmail.com)
	* Since : 2020-07-06
*/

#include <stdio.h>

int main(void)
{
	int i;
	int x, y;
	int burger[3];
	int drink[2];

	for (i = 0; i < 3; i++)
		scanf("%d", &burger[i]);

	for (i = 0; i < 2; i++)
		scanf("%d", &drink[i]);

	x = 2000;
	for (i = 0; i < 3; i++)
	{
		if (burger[i] < x)
			x = burger[i];
	}

	if (drink[0] < drink[1])
		y = drink[0];
	else
		y = drink[1];

	printf("%d\n", x + y - 50);

	return 0;
}
