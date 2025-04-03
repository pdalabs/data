#include<stdio.h>
#include<time.h>
int partition (int a[],int low , int high);
void quicksort(int a[],int low,int high)
{
int j;
if (low<high)
{
j=partition(a,low,high);
quicksort(a,low,j-1);
quicksort(a,j+1,high);
}
}
int partition(int a[],int low,int high)
{
int i,j,temp,key;
key=a[low];
i=low+1;
j=high;
while(1)
{
while(i<high && key>=a[i])
i++;
while(key<a[j])
j--;
if (i<j)
{
temp=a[i];
a[i]=a[j];
a[j]=temp;
}
else
{
temp=a[low];
a[low]=a[j];
a[j]=temp;
return j;
}
}
}

void main()
{
int i,n,a[20];
float f; 
clock_t start, end;
printf("Enter the number of Elements\n");
scanf("%d",&n);
printf("Enter the[%d] elements:\n",n);
for(i=0;i<n;i++);
scanf("%d",&a[i]);
start=clock();
quicksort(a,0,n-1);
end=clock();
printf("\n The sorted array is:\n");
for(i=0;i<n;i++)
printf("%d\t",a[i]);
printf("\nTime taken =%f",(double)(end-start)/CLOCKS_PER_SEC);
}
