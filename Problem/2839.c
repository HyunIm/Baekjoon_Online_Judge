/**
 * File : 2839.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2018 - 12 - 07
*/

#include <stdio.h>

int main(void)
{
	int i;
	int sugar;
	int three = 0;
	int five = -1;

	scanf("%d", &sugar);

	for (i = sugar / 5; i >= 0; i--)
	{
		if ((sugar - (5 * i)) % 3 == 0)
		{
			five = i;
			three = (sugar - (5 * i)) / 3;

			break;
		}
	}

	printf("%d\n", three + five);

	return 0;
}

/*
==== 경우의 수 ====
 1. 5킬로그램 봉지로 최대한 채운 뒤 3킬로그램 봉지로 해결하는 경우
	-> 5킬로그램 봉지만 있을 수도 있음
	-> 3킬로그램 봉지가 여러개 일 수도 있음
	-> 5킬로그램 봉지가 하나도 없을 수도 있음
 2. 해결하지 못 하는 경우
*/