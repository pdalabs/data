#include<stdio.h>
#include<time.h>
#define max 20
int ls(int,int);
int bs(int,int,int);
int a[max],n,key;
int main()
{
int i,key,ch,mid,low,high,l;
clock_t start1,end1,start2,end2;
printf("enter te limit\n");
scanf("%d",&n);
printf("enter the elements\n");
for(i=1;i<=n;i++)
scanf("%d",&a[i]);
printf("\n LINEAR SEARCH \\n");
start1=clock();
printf("enter the key element to search\n");
scanf("%d",&key);
l=ls(1,key);
end1=clock();
if(l==-1)
printf("elements is not found\n");
else
printf("elements is found\n");
printf("time=%f",((double)(end1-start1))/(clocks_per_sec));
start2=clock();
printf("enter the key elements to be searched\n");
scanf("%d",&key);
low=1;
high=n;
ch=bs(low,high,key);
end2=clock();
if(ch==-1)
printf("elements is not found\n");
else
printf("elements is found\n");
printf("time=%f",((double)(end2-start2))/clocks_per_sec);
}
int ls(int i,int key);
{
if(i>n)
return(-1);
if(a[i]==key)
return i;
else
ls(++i,key);
return 0;
}
int bs(int low,int high,int key)
{
int mid;
if(low>high)
return(-1);
mid=(low+high)/2;
if(a[mid]==key)
return mid;
else
{
if(key<a[mid])
bs(low,mid-1,key);
else
bs(mid+1,high,key);
}
}
