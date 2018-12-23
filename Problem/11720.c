/**
 * File : 11720.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2018 - 12 - 23
*/

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int i, n;
	int sum = 0;
	char m[100];	// 오버플로우 문제 때문에 string으로 처리

	scanf("%d %s", &n, &m);

	for (i = 0; i < n; i++)
		sum += (m[i] - '0');

	printf("%d\n", sum);

	return 0;
}