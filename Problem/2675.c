/**
 * File : 2675.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 06
*/

#include <stdio.h>
#include <string.h>

int main(void)
{
	int i, j, k;
	int t;	// 테스트 케이스의 개수
	int r;	// 반복 횟수
	int size;	// 문자열의 길이
	char s[20];	// 문자열

	scanf("%d", &t);

	for (i = 0; i < t; i++)
	{
		scanf("%d", &r);

		scanf("%s", s);

		size = strlen(s);

		for (j = 0; j < size; j++)
		{
			for (k = 0; k < r; k++)
				printf("%c", s[j]);
		}
		printf("\n");
	}
	
	return 0;
}
