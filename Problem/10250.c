/**
 * File : 10250.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 27
*/

#include <stdio.h>

int main(void)
{
	int i, j, k;
	int t;
	int h, w, n;
	int result;

	scanf("%d", &t);

	while (t)
	{
		scanf("%d %d %d", &h, &w, &n);

		j = 1;
		k = 1;
		for (i = 0; i < n; i++)
		{
			if (j > h)
			{
				j = 1;
				k++;
			}
			j++;
		}
		j--;

		result = (j * 100) + k;
		printf("%d\n", result);

		t--;
	}

	return 0;
}
