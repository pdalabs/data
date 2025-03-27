#include<stdio.h>
#include<time.h>
int mergesort (int *, int ,int);
int merge(int *, int ,int,int);
void main(){
int i,n,a[20];
clock_t start,end;
start=clock();
printf("Enter the limits\n");
scanf("%d",&n);
printf("Enter the elements\n");
for(i=0;i<n;i++)
scanf("%d",&a[i]);
mergesort (a,0,n-1);
end=clock();
printf("Enter sorted elements\n");
for(i=0;i<n;i++)
printf("%d\n", a[i]);
printf("\n Time=%f",((double)(end-start))/CLOCKS_PER_SEC);
return ;
}
int mergesort(int a[],int low,int high)
{
int mid;
if (low<high)
{
mid=(low+high)/2;
mergesort(a,low,mid);
mergesort(a,mid+1,high);
merge(a,low,mid,high);
}
}
int merge(int a[],int low,int mid,int high)
{
int i,j,k,h,b[20];
h=i=low;
j=mid+1;
while(h<=mid && j<=high)
if(a[h]<a[j])
b[i++]=a[h++];
else
b[i++]=a[j++];
if(h>mid)
for(k=j;k<=high;k++)
b[i++]=a[k];
else
for(k=h;k<=mid;k++)
b[i++]=a[k];
for(k=low;k<=high;k++)
a[k]=b[k];
}

