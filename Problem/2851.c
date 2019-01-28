/**
 * File : 2851.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 29
*/

#include <stdio.h>
#include <math.h>

int main(void)
{
	int i;
	int mushroom;
	int result = 0;

	for (i = 0; i < 10; i++)
	{
		scanf("%d", &mushroom);

		result += mushroom;

		if (result >= 100)
			break;
	}

	if (abs(result - 100) <= abs(100 - (result - mushroom)))
	{
		printf("%d\n", result);
	}
	else
	{
		printf("%d\n", result - mushroom);
	}

	return 0;
}
