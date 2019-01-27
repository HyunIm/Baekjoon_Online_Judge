/**
 * File : 1475.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 27
*/

#include <stdio.h>

int main(void)
{
	int i;
	int n;
	int x;
	int result = 1;
	int set[10];

	for (i = 0; i < 10; i++)
		set[i] = 1;

	scanf("%d", &n);

	while (n)
	{
		x = n % 10;
		n /= 10;

		if (set[x] == 0)
		{
			if (x == 6)
			{
				if (set[9] > 0)
				{
					set[9]--;
					continue;
				}
			}

			else if (x == 9)
			{
				if (set[6] > 0)
				{
					set[6]--;
					continue;
				}
			}

			result++;

			for (i = 0; i < 10; i++)
				set[i]++;

			set[x]--;
		}

		else
		{
			set[x]--;
		}
	}

	printf("%d\n", result);

	return 0;
}
