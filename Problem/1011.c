/**
 * File : 1011.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 25
*/

#include <stdio.h>
#include <math.h>	// sqrt()

int main(void)
{
	int i, j;
	int t;	// 테스트케이스의 개수
	int x, y;	// 현재 위치 x, 목표 위치 y
	int dist;	// y - x (거리)
	int cnt;	// 공간이동 장치 작동 회수
	int k;

	scanf("%d", &t);
	// t = 1;
	for (i = 0; i < t; i++)
	{
		cnt = 0;	// 초기화

		scanf("%d %d", &x, &y);
		// x = 0;
		// scanf("%d", &y);

		dist = y - x;
		k = sqrt((double)dist);

		cnt += 2 * k - 1;

		dist -= k * k;

		if (dist != 0)
		{
			cnt += dist / k;

			if (dist % k != 0)
			{
				cnt++;
			}
		}

		else
		{
			printf("%d\n", cnt);
			continue;
		}

		printf("%d\n", cnt);
	}

	return 0;
}

/*
 ================================
	1	1	1
	2	2	1 1
	3	3	1 1 1
	4	3	1 2 1
	5	4	1 2 1 1
	6	4	1 2 2 1
	7	5	1 2 2 1 1
	8	5	1 2 2 2 1
	9	5	1 2 3 2 1
	10	6	1 2 2 2 2 1
	11	6	1 2 3 2 2 1
	12	6	1 2 3 3 2 1
	13	7	1 2 3 2 2 2 1
	14	7	1 2 3 3 2 2 1
	15	7	1 2 3 3 3 2 1
	16	7	1 2 3 4 3 2 1
	17	8	1 2 3 4 3 2 1 1
	18	8	1 2 3 4 3 2 2 1
	19	8	1 2 3 4 3 3 2 1
	20	8	1 2 3 4 4 3 2 1
	21	9	1 2 3 4 3 3 2 2 1
 ================================
*/
