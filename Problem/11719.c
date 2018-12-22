/**
* File : 11719.c
* Author : 임현 (hyunzion@gmail.com)
* Since : 2018 - 12 - 04
*/

#include <stdio.h>

int main(void)
{
	char c;

	c = getchar();

	while (c != EOF)
	{
		putchar(c);

		c = getchar();
	}

	return 0;
}