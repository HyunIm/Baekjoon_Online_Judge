/**
 * File : 11721.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2018 - 12 - 25
*/

#include <stdio.h>

int main(void)
{
	int i = 0;
	char str[100];

	scanf("%s", str);

	while (str[i] != NULL)
	{
		printf("%c", str[i]);

		if (i % 10 == 9)
			printf("\n");

		i++;
	}

	return 0;
}