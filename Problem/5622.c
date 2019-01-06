/**
 * File : 5622.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 06
*/

#include <stdio.h>
#include <string.h>

int main(void)
{
	int i;
	int size;
	int time = 0;
	int phone[26] = { 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10 };
	char word[16];

	scanf("%s", word);

	size = strlen(word);
	for (i = 0; i < size; i++)
	{
		time += phone[word[i] - 'A'];
	}

	printf("%d\n", time);

	return 0;
}
