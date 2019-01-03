/**
 * File : 1152.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 03
*/

#include <stdio.h>
#include <string.h>	// strlen

int main(void)
{
	int i;
	int size;		// 문자열 크기
	int cnt = 1;	// 단어들 개수
	char str[1000000];	// 문자열

	scanf("%[^\n]", str);	// 띄어쓰기도 받기 위함

	size = strlen(str);	// 문자열 크기 계산

	if (str[0] == ' ')	// 처음에 띄어쓰기가 있을 경우
		cnt--;
	if (str[size - 1] == ' ')	// 마지막에 띄어쓰기가 있을 경우
		cnt--;
	
	for (i = 0; i < size; i++)
	{
		if (str[i] == ' ')	// 스페이스가 나오면 단어 개수 추가
			cnt++;
	}

	printf("%d\n", cnt);


	return 0;
}
