﻿/**
* File : 10430.c
* Author : 임현 (hyunzion@gmail.com)
* Since : 2018 - 12 - 06
*/

#include <stdio.h>

int main(void)
{
	int A, B, C;

	scanf("%d %d %d", &A, &B, &C);

	printf("%d\n", (A + B) % C);
	printf("%d\n", (A % C + B % C) % C);
	printf("%d\n", (A * B) % C);
	printf("%d\n", (A % C * B % C) % C);

	return 0;
}