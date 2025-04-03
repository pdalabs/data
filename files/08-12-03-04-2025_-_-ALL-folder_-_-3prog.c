#include<stdio.h>
#include<stdlib.h>

int a[20][20], reach[20], n;

void dfs(int v)
{
	int i;
	reach[v] = i;
	for(i = 1; i <= n; i++)
	{
		if (a[v][i] && !reach[i])
		{
			printf("\n%d-->%d", v, i);
			dfs(i);
		}
	}
}

void main()
{
	system("clear");
	int i, j, count = 0;
	printf("enter the number of vertices:");
	scanf("%d",&n);
	for(i = 1; i <= n; i++)
	{
		reach[i]=0;
		for(j=1;j<=n;j++)
			a[i][j]=0;
	}
	printf("enter the adjacent matrix\n");
	for(i = 1; i <= n ; i++)
	{
		for(j = 1; j <= n; j++)
			scanf("%d", &a[i][j]);
	}
	dfs(1);
	printf("\n");
	for(i = 1; i <= n; i++)
	{
		if(reach[i])
			count++;
	}
	if(count == n)
		printf("\n graph is connected:");
	else
		printf("\ngraph is not connected:");
}
