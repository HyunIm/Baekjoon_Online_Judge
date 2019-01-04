/**
 * File : 10039.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 04
*/

#include <stdio.h>

int main(void)
{
	int i;
	int sum = 0;
	int score[5];

	for (i = 0; i < 5; i++)
	{
		scanf("%d", &score[i]);

		if (score[i] < 40)
			score[i] = 40;

		sum += score[i];
	}

	sum /= 5;

	printf("%d\n", sum);
	
	return 0;
}
