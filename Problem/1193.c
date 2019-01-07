/**
 * File : 1193.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 08
*/

#include <stdio.h>

int main(void)
{
	int x;
	int up = 2;
	int down = 0;
	int up_chk = 2;
	int down_chk = 1;
	unsigned flag = 0;

	scanf("%d", &x);

	while (x)
	{
		if (up == 1)
		{
			up_chk++;
			up = up_chk;
		}

		up--;
		down++;

		if (down == down_chk)
		{
			down = 1;
			down_chk++;
			flag = ~flag;
		}

		x--;
	}

	if (flag == 0)
		printf("%d/%d\n", down, up);
	else
		printf("%d/%d\n", up, down);

	return 0;
}
