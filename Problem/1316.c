/**
 * File : 1316.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 06
*/

#include <stdio.h>
#include <string.h>

int main(void)
{
	int i, j;
	int n;
	int size;
	int cnt = 0;
	int alphabet[26];
	char word[100];

	scanf("%d", &n);

	for (i = 0; i < n; i++)
	{
		scanf("%s", word);

		for (j = 0; j < 26; j++)
			alphabet[j] = 0;

		size = strlen(word);
		for (j = 0; j < size; j++)
		{
			if (alphabet[word[j] - 'a'] > 0)
			{
				if (word[j - 1] == word[j])
				{
					continue;
				}

				else
				{
					cnt--;
					break;
				}
			}

			else
			{
				alphabet[word[j] - 'a']++;
			}
		}

		cnt++;
	}

	printf("%d\n", cnt);
	
	return 0;
}
