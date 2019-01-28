/**
 * File : 1780.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 29
*/

#include<stdio.h>
#include<malloc.h>

int c1, c2, c3;

void dac(int is, int js, int num, int **arr);

int main(void)
{
	int i, j;
	int num;
	int **arr;

	scanf("%d", &num);

	arr = (int **)malloc(sizeof(int*) * num);
	for (i = 0; i < num; i++)
		arr[i] = (int *)malloc(sizeof(int) * num);

	for (i = 0; i < num; i++)
		for (j = 0; j < num; j++)
			scanf("%d", &arr[i][j]);

	dac(0, 0, num, arr);

	printf("%d\n", c1);
	printf("%d\n", c2);
	printf("%d\n", c3);

	for (i = 0; i < num; i++)
		free(arr[i]);
	free(arr);

	return 0;
}

void dac(int is, int js, int num, int **arr)
{
	int i, j;
	int flag = 0;

	for (i = is; i < is + num; i++)
	{
		for (j = js; j < js + num; j++)
		{
			if (arr[is][js] != arr[i][j])
			{
				dac(is, js, num / 3, arr);
				dac(is + num / 3, js, num / 3, arr);
				dac(is + ((2 * num) / 3), js, num / 3, arr);

				dac(is, js + num / 3, num / 3, arr);
				dac(is + num / 3, js + num / 3, num / 3, arr);
				dac(is + ((2 * num) / 3), js + num / 3, num / 3, arr);

				dac(is, js + ((2 * num) / 3), num / 3, arr);
				dac(is + num / 3, js + ((2 * num) / 3), num / 3, arr);
				dac(is + ((2 * num) / 3), js + ((2 * num) / 3), num / 3, arr);

				flag = 1;

			}
			if (flag == 1) {
				break;
			}
		}
		if (flag == 1) {
			break;
		}
	}

	if (flag == 0)
	{
		if (arr[is][js] == -1)
			c1++;
		else if (arr[is][js] == 0)
			c2++;
		else if (arr[is][js] == 1)
			c3++;
	}
}
