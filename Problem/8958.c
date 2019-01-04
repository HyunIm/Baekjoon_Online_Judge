/**
 * File : 8958.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 04
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	int i, j;
	int n;
	int bonus;
	int score;
	int size;
	char result[80];

	scanf("%d", &n);

	for (i = 0; i < n; i++)
	{
		scanf("%s", result);

		score = 0;
		bonus = 1;

		size = strlen(result);
		for (j = 0; j < size; j++)
		{
			if (result[j] == 'O')
			{
				score += bonus;
				bonus++;
			}

			else
			{
				bonus = 1;
			}
		}

		printf("%d\n", score);
	}

	return 0;
}
