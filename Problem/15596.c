/**
 * File : 15596.c
 * Author : LimHyun (hyunzion@gmail.com)
 * Since : 2019 - 10 - 20
*/

long long sum(int *a, int n)
{
	int i;
	long long ans = 0;

	for (i = 0; i < n; i++)
	{
		ans += (long long)a[i];
	}

	return ans;
}
