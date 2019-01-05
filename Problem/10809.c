/**
 * File : 10809.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 06
*/

#include <stdio.h>
#include <string.h>

int main(void)
{
	int i;
	int size;
	int alphabet[26];
	char word[100];

	for (i = 0; i < 26; i++)
		alphabet[i] = -1;

	scanf("%s", word);

	size = strlen(word);
	for (i = 0; i < size; i++)
	{
		if (alphabet[word[i] - 'a'] == -1)
			alphabet[word[i] - 'a'] = i;
	}

	for (i = 0; i < 26; i++)
		printf("%d ", alphabet[i]);
	
	return 0;
}
