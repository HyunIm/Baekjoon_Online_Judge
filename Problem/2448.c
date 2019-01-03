/**
 * File : 2448.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 01
*/

#include <stdio.h>

char star[3072][6143];

void PrintStar(int n, int x, int y);

int main(void)
{
	int i, j;
	int n;

	scanf("%d", &n);

	for (i = 0; i < n; i++)
	{
		for (j = 0; j < 2 * n - 1; j++)
		{
			star[i][j] = ' ';
		}
	}

	PrintStar(n, n - 1, 0);

	for (i = 0; i < n; i++)
	{
		for (j = 0; j < 2 * n - 1; j++)
		{
			printf("%c", star[i][j]);
		}
		printf("\n");
	}

	return 0;
}

void PrintStar(int n, int x, int y)
{
	if (n == 3)
	{
		star[y][x] = '*';

		star[y + 1][x - 1] = '*';
		star[y + 1][x + 1] = '*';

		star[y + 2][x - 2] = '*';
		star[y + 2][x - 1] = '*';
		star[y + 2][x] = '*';
		star[y + 2][x + 1] = '*';
		star[y + 2][x + 2] = '*';
	}

	else
	{
		PrintStar(n / 2, x, y);
		PrintStar(n / 2, x - n / 2, y + n / 2);
		PrintStar(n / 2, x - n / 2 + n, y + n / 2);
	}
}
