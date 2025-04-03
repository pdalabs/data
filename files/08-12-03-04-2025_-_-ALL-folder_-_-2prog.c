#include<stdio.h>
#include<time.h>
#include<stdlib.h>

int selection_sort(int a[], int n);

int main()
{
	system("clear");
	int i, n, a[20], key;
	clock_t end, start;
	printf("enter the size of array\n");
	scanf("%d",&n);
	printf("enter the array elements\n");
	for(i = 0; i < n; i++)
		scanf("%d", &a[i]);
	start = clock();
	selection_sort(a, n);
	end = clock();
	printf("sorted elements are\n");
	for(i=0; i<n; i++)
	printf("\n%d", a[i]);
	printf("\nTime=%f", (double)(end-start)/CLOCKS_PER_SEC);
}

int selection_sort(int a[], int n)
{
	int i, j, pos, small, temp;
	for(i = 0; i < n - 1; i++)
	{
		small = a[i];
		pos = i;
		for(j = i+1; j < n; j++)
		{
			if(a[j] < small)
			{
				small = a[j];
				pos = j;
			}
		}
		temp = a[pos];
		a[pos] = a[i];
		a[i] = temp;
	}
}
