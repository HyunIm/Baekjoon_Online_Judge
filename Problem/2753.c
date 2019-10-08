/**
 * File : 2753.c
 * Author : LimHyun (hyunzion@gmail.com)
 * Since : 2019 - 10 - 08
*/

#include <stdio.h>

int main(void)
{
	int year;
	int leap = 0;

	scanf("%d", &year);

	if (year % 4 == 0)
	{
		leap = 1;
		if (year % 100 == 0)
		{
			leap = 0;
			if (year % 400 == 0)
			{
				leap = 1;
			}
		}
	}

	printf("%d\n", leap);

	return 0;
}
