/**
 * File : 2588.c
 * Author : LimHyun (hyunzion@gmail.com)
 * Since : 2019 - 10 - 06
*/

#include <stdio.h>

int main(void)
{
	int num[6];
	int i;

	scanf("%d", &num[0]);
	scanf("%d", &num[1]);

	num[5] = num[0] * num[1];

	i = 2;
	while (num[1] > 0)
	{
		num[i] = num[0] * (num[1] % 10);
		num[1] /= 10;

		i++;
	}

	for (i = 2; i < 6; i++)
	{
		printf("%d\n", num[i]);
	}

	return 0;
}
