/**
 * File : 1065.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 01
*/

#include <stdio.h>

int HanNumber(int n);

int main(void)
{
	int n;

	scanf("%d", &n);

	printf("%d\n", HanNumber(n));

	return 0;
}

int HanNumber(int n)
{
	int nn;	// 해당 한수 계산 용
	int cnt = 0;	// 한수의 개수
	int cip = 0;	// 자릿수 계산
	int num[3] = { 0, };	// 각 자릿수 배열

	while (n)
	{
		if (n < 100)	// 100 미만은 무조건 한수
			cnt++;

		else if (n == 1000)	// 1000은 무조건 한수 X
		{
			n--;
			continue;
		}

		else	// 100 ~ 999
		{
			nn = n;	// 해당 n 저장
			cip = 0;	// 자릿수 계산용

			while (nn)	// 각 자릿수 계산
			{
				num[cip] = nn % 10;
				nn /= 10;
				cip++;
			}
			
			// 등차 수열 계산
			if ((num[0] - num[1]) == (num[1] - num[2]))
				cnt++;	// 등차수열일 경우 ++
		}

		n--;
	}

	return cnt;
}
