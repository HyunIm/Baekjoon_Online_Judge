/**
 * File : 2920.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 04
*/

#include <stdio.h>

int main(void)
{
	int i;
	int flag = 0;
	int sound[8];

	for (i = 0; i < 8; i++)
		scanf("%d", &sound[i]);

	for (i = 0; i < 8; i++)
	{
		if (sound[i] == (i + 1))
		{
			flag++;
			continue;
		}

		else if (sound[i] == (8 - i))
		{
			flag--;
			continue;
		}

		else
		{
			flag = 0;
			break;
		}
	}

	if (flag == -8)
		printf("descending\n");
	else if (flag == 8)
		printf("ascending\n");
	else
		printf("mixed\n");
	
	return 0;
}
