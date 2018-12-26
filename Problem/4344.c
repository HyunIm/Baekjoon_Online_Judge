/**
 * File : 4344.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2018 - 12 - 27
*/

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int i, j;	// for문 용도
	int c;	// 테스트 케이스 개수
	int n;	// N명의 점수
	int sum = 0;	// N명의 점수 합
	int cnt = 0;	// 평균을 넘는 학생 수
	int avg;	// N명의 평균
	int *arr;	// N명의 점수들

	scanf("%d", &c);

	for (i = 0; i < c; i++)
	{
		scanf("%d", &n);

		arr = (int *)malloc(sizeof(int) * n);

		for (j = 0; j < n; j++)
		{
			scanf("%d", &arr[j]);
			sum += arr[j];
		}

		avg = sum / n;

		for (j = 0; j < n; j++)
		{
			if (arr[j] > avg)
				cnt++;
		}

		printf("%.3f%%\n", (float)cnt * 100.000 / n);	// *와 /의 순서도 중요함

		sum = 0;
		cnt = 0;

		free(arr);
	}

	return 0;
}
