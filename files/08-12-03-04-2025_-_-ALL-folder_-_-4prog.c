#include<stdio.h>
#include<stdlib.h>

int i, j, n, r = -1, f, q[20], visited[20];
int a[20][20];
int bfs(int v);

void main()
{
	int v;
	printf("Enter the number of vertices...\n");
	scanf("%d",&n);
	for(i = 1; i <= n; i++)
	{
		q[i] = 0;
		visited[i] = 0;
	}
	printf("Enter the adjacency matix..\n");
	for(i = 1; i <= n; i++)
	{
		for(j = 1; j <= n; j++)
			scanf("%d", &a[i][j]);
	}
	printf("Enter the starting vertex...\n");
	scanf("%d", &v);
	bfs(v);
	printf("The nodes that are reachable from given node %d are..\n", v);
	for(i = 1; i <= n; i++)
	{
		if(visited[i])
			printf("%d", i);
	}
}

int bfs(int v)
{
	for(i=1;i<=n;i++)
		if(a[v][i] && ! visited[j])
			q[++r]=i;
			visited[i]=1;
	if(f<=r)
	{
		visited[q[f]]=1;
		bfs(q[f++]);
	}
}

