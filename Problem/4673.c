/**
 * File : 1110.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2018 - 12 - 31
*/

#include <stdio.h>

int self_number[10001];		// 셀프 넘버 배열 (1일 경우 셀프 넘버 X)

int selfNumberCheck(int n);	// 셀프 넘버 체크 함수 (반환 값은 셀프 넘버가 아닌 수들)

int main(void)
{
	int i;
	
	for (i = 1; i <= 10000; i++)
	{
		self_number[selfNumberCheck(i)] = 1;

		if (!self_number[i])
			printf("%d\n", i);
	}

	return 0;
}

int selfNumberCheck(int n)
{
	int sn = 0;

	sn += n;

	while (n)
	{
		sn += n % 10;
		n /= 10;
	}

	return sn;
}
