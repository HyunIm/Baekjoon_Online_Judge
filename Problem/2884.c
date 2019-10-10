/**
 * File : 2884.c
 * Author : LimHyun (hyunzion@gmail.com)
 * Since : 2019 - 10 - 10
*/

#include <stdio.h>

int main(void)
{
	int h, m;

	scanf("%d", &h);
	scanf("%d", &m);

	m -= 45;

	if (m < 0)
	{
		m += 60;
		h -= 1;
	}

	if (h < 0)
	{
		h += 24;
	}

	printf("%d %d\n", h, m);

	return 0;
}
