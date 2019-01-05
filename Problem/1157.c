/**
 * File : 1157.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 06
*/

#include <stdio.h>
#include <string.h>

int main(void)
{
	int i;
	int size;
	int max = -1;
	int loc = 0;
	int freq[26] = { 0, };
	char word[1000000];

	scanf("%s", word);

	size = strlen(word);
	for (i = 0; i < size; i++)
	{
		if ('a' <= word[i] && word[i] <= 'z')
			freq[word[i] - 'a']++;
		else
			freq[word[i] - 'A']++;
	}

	for (i = 0; i < 26; i++)
	{
		if (max == freq[i])
		{
			max = freq[i];
			loc = -1;
		}

		else if (max < freq[i])
		{
			max = freq[i];
			loc = i;
		}
	}

	if (loc == -1)
		printf("?");
	else
		printf("%c", loc + 'A');
	
	return 0;
}
