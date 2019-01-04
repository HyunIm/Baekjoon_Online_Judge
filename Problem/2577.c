/**
 * File : 2577.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 04
*/

#include <stdio.h>

int main(void)
{
	int i;
	int a, b, c;
	int result;
	int cnt[10] = { 0, };

	scanf("%d %d %d", &a, &b, &c);

	result = a * b * c;

	while (result)
	{
		i = result % 10;
		result /= 10;

		cnt[i]++;
	}

	for (i = 0; i < 10; i++)
		printf("%d\n", cnt[i]);

	return 0;
}
