/**
 * File : 1924.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2018 - 12 - 23
*/

#include <stdio.h>

int main(void)
{
	int i;
	int x, y;
	int count = 0;
	int month[12] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30};
	char *day[7] = { "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT" };

	scanf("%d %d", &x, &y);
	
	count += y;

	for (i = 0; i < x; i++)
		count += month[i];

	printf("%s\n", day[count% 7]);

	return 0;
}