/**
* File : 2839.c
* Author : 임현 (hyunzion@gmail.com)
* Since : 2018 - 12 - 07
*/

#include <stdio.h>

void Delivery(int sugar);

int main(void)
{
	int sugar;

	scanf("%d", &sugar);

	Delivery(sugar);

	return 0;
}

void Delivery(int sugar)
{
	int i;
	int five, three;	// 5킬로그램 봉지, 3킬로그램 봉지
	int flag = -1;	// 해결 할 수 없는 경우의 수 체크

	for (i = sugar / 5; i >= 0; i--)
	{
		if ((sugar - (5 * i)) % 3 == 0)	// 5킬로그램 봉지로 최대한 채운 뒤 3킬로그램 봉지 빼기
		{
			five = i;
			three = ((sugar - (5 * five)) / 3);
			printf("%d\n", five + three);

			flag = 1;	// 해결 되는 경우
			break;
		}
	}

	if (flag == -1)	// 해결 불가능한 경우
		printf("-1\n");
}

/*
==== 경우의 수 ====
 1. 5킬로그램 봉지로 최대한 채운 뒤 3킬로그램 봉지로 해결하는 경우
	-> 5킬로그램 봉지만 있을 수도 있음
	-> 3킬로그램 봉지가 여러개 일 수도 있음
	-> 5킬로그램 봉지가 하나도 없을 수도 있음
 2. 해결하지 못 하는 경우
*/