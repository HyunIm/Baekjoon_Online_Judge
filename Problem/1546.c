/**
 * File : 1546.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2018 - 12 - 27
*/

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int i;	// for문 용도
	int n;	// 과목의 개수
	int max = 0;	// 최고점
	float sum = 0;	// 과목 점수 합
	int *arr;	// 각 괌고 점수

	scanf("%d", &n);

	arr = (int *)malloc(sizeof(int) * n);

	for (i = 0; i < n; i++)
	{
		scanf("%d", &arr[i]);
		
		if (max < arr[i])
			max = arr[i];
	}

	for (i = 0; i < n; i++)
		sum += ((float)arr[i] / max * 100);

	sum /= n;

	printf("%.2f\n", sum);

	free(arr);

	return 0;
}
