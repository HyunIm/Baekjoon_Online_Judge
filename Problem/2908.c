/**
 * File : 2908.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 06
*/

#include <stdio.h>
#include <stdlib.h>

void swap(char *x, char *y);

int main(void)
{
	char a[4];
	char b[4];

	scanf("%s %s", a, b);

	swap(&a[0], &a[2]);
	swap(&b[0], &b[2]);

	if (atoi(a) > atoi(b))
		printf("%s", a);
	else
		printf("%s", b);
	
	return 0;
}

void swap(char *x, char *y)
{
	char tmp;

	tmp = *x;
	*x = *y;
	*y = tmp;
}
