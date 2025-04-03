#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<unistd.h>
#define max 20

int ls(int i, int key);
int bs(int low, int high, int key);

int a[max], key, n;

/*void delay()
{
	usleep(500000);
}

void anime()
{
	char anime[] = {'-', '/', '|', '\\', '-'};
	for(int i = 0; i < 2; i++)
	{
		for(int j = 0; j < 5; j++)
		{
			printf("\b%c", anime[i]);
			fflush(stdout);
			delay();
		}
	} 
}*/

void main()
{
	system("clear");
	int i, ch, mid, low, high, L;
	clock_t start1, end1, start2, end2;
	printf("Enter the limit: ");
	scanf("%d", &n);
	printf("Enter the elements: \n");
	for(i = 1; i <= n; i++)
	{
		scanf("%d", &a[i]);
	}
	//anime();
	//printf("\nElements has been accepted");
	
	printf("\nLINEAR SEARCH \n ");
	start1 = clock();
	printf("Enter the key element to search: \n");
	scanf("%d", &key);
	L = ls(1, key);
	end1 = clock();
	if(L == -1)
		printf("Element is not found\n");
	else
	{
		printf("Element is found\n");
		printf("The index of the element is %d\n", L);
	}
	printf("Time = %f", ((double)(end1 - start1))/CLOCKS_PER_SEC);
	printf("\n");
	printf("\nBINARY SEARCH\n");
	start2 = clock();
	printf("Enter the key element to be searched\n");
	scanf("%d", &key);
	low = 1;
	high = n;
	ch = bs(low, high, key);
	end2 = clock();
	if (ch == -1)
		printf("Element is not found\n");
	else
	{
		printf("Element is found\n");
		printf("The index of the element is %d\n", ch);
	}
	printf("Time = %f\n", ((double)(end1 - start1))/CLOCKS_PER_SEC);
}

int ls(int i, int key)
{
	if(i > n)
		return(-1);
	if(a[i] == key)
		return i;
	else
		ls(++i, key);
}

int bs(int low, int high, int key)
{
	int mid;
	if(low > high)
		return(-1);
	mid = (low + high)/2;
	if(a[mid] == key)
		return mid;
	else
	{
		if(key < a[mid])
			bs(low, mid - 1, key);
		else
			bs(mid + 1, high, key);
	}
}

