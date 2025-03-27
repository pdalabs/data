#include<stdio.h>
#include<time.h>
void selection_sort(int arr[],int n)
{
int i,j,minindex,temp;
for(i=0;i<n-1;i++)
{
minindex=i;
for(j=i+1;j<n;j++)
{
if(arr[j]<arr[minindex])
{
minindex=j;
}
}
temp=arr[minindex];
arr[minindex]=arr[i];
arr[i]=temp;
}
}
int main()
{
int n,i;
clock_t start,end;
double cpu_time_used;
printf("Enter the number of elements:");
scanf("%d",&n);
int arr[n];
printf("Enter %d elements :\n",n);
for(i=0;i<n;i++)
{
scanf("%d",&arr[i]);
}
start=clock();
selection_sort(arr,n);
end=clock();
cpu_time_used = ((double)(end-start))/CLOCKS_PER_SEC;
printf("Sorted elements:");
for(i=0;i<n;i++)
{
printf("%d",arr[i]);
}
printf("\n");
printf("Time taken to sort : %f seconds\n",cpu_time_used);


return 0;
}
