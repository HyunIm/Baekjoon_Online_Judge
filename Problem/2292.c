/**
 * File : 2292.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 07
*/

#include <stdio.h>

int main(void)
{
	int n;
	int six = 1;
	int cnt = 1;

	scanf("%d", &n);

	while (1)
	{
		if (n <= six)
			break;	

		six += 6 * cnt;
		cnt++;
	}

	printf("%d\n", cnt);

	return 0;
}
