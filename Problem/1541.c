/**
 * File : 1541.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 29
*/

#include <stdio.h>

int main(void)
{
	int num;
	int result = 0;
	int flag = 0;
	char ch;

	while (1)
	{
		scanf("%d%c", &num, &ch);

		if (flag == 0)
		{
			result += num;
		}
		else
		{
			result -= num;
		}

		if (ch == '-')
		{
			flag = 1;
		}
		else if (ch == '\n')
		{
			break;
		}
	}

	printf("%d\n", result);

	return 0;
}
