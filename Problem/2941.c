/**
 * File : 2941.c
 * Author : 임현 (hyunzion@gmail.com)
 * Since : 2019 - 01 - 06
*/

#include <stdio.h>
#include <string.h>

int main(void)
{
	int i;
	int size;
	int cnt = 0;
	char word[101];

	scanf("%s", word);

	size = strlen(word);
	for (i = 0; i < size; i++)
	{
		if (word[i] == 'c' && word[i + 1] == '=')
			continue;
		else if (word[i] == 'c' && word[i + 1] == '-')
			continue;
		else if (word[i] == 'd' && word[i + 1] == 'z' && word[i + 2] == '=')
			continue;
		else if (word[i] == 'd' && word[i + 1] == '-')
			continue;
		else if (word[i] == 'l' && word[i + 1] == 'j')
			continue;
		else if (word[i] == 'n' && word[i + 1] == 'j')
			continue;
		else if (word[i] == 's' && word[i + 1] == '=')
			continue;
		else if (word[i] == 'z' && word[i + 1] == '=')
			continue;
		cnt++;
	}

	printf("%d\n", cnt);

	return 0;
}
