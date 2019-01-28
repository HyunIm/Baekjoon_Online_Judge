/**
 * File : 6064.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 29
*/

#include <stdio.h>

int Cain(int m, int n, int x, int y);

int main(void)
{
	int t;
	int m, n, x, y;
	int k;

	scanf("%d", &t);

	while (t)
	{
		scanf("%d %d %d %d", &m, &n, &x, &y);

		k = Cain(m, n, x, y);

		printf("%d\n", k);
		t--;
	}

	return 0;
}

int Cain(int m, int n, int x, int y)
{
	int k;
	int cal_y;
	int end = m * n;

	k = x;

	if (x % n == 0)
	{
		cal_y = n;
	}
	else
	{
		cal_y = x % n;
	}
		
	while (1)
	{
		if (cal_y == y)
		{
			return k;
		}

		if (k >= end)
		{
			return -1;
		}
		
		if ((cal_y + m) % n)
		{
			cal_y = (cal_y + m) % n;
		}
		else
		{
			cal_y = n;
		}

		k += m;
	}
}

// ==== 시간 초과 ====
/*
int main(void)
{
	int t;
	int m, n, x, y;
	int k;
	int a, b;
	int end;

	scanf("%d", &t);

	while (t)
	{
		scanf("%d %d %d %d", &m, &n, &x, &y);

		a = 1;
		b = 1;
		k = 1;
		end = (m * n);
		while (1)
		{
			if (a == x && b == y)
			{
				break;
			}

			if (k == end)
			{
				k = -1;
				break;
			}

			if (a == m)
			{
				a = 0;
			}

			if (b == n)
			{
				b = 0;
			}

			a++;
			b++;
			k++;
		}

		printf("%d\n", k);

		t--;
	}

	return 0;
}
*/
