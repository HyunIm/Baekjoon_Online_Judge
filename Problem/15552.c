﻿/**
 * File : 15552.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2018 - 12 - 25
*/

#include <stdio.h>

int main(void)
{
	int i, t, a, b;

	scanf("%d", &t);

	for (i = 0; i < t; i++)
	{
		scanf("%d %d", &a, &b);

		printf("%d\n", a + b);
	}

	return 0;
}