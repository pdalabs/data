#include<stdio.h>
int gcdEuclid(int a, int b);
int gcdMiddleSchool(int a,int b);
int gcdPrimeFactorization(int a,int b);
int main()
{
int num1, num2;
printf("enter first number: ");
scanf("%d", &num1);
printf("enter second number: ");
scanf("%d", &num2);
printf("GCD using Euclid's algorithm: %d",gcdEuclid(num1,num2));
printf("GCD using Middle School algorithm: %d",gcdMiddleSchool(num1,num2));
printf("GCD using Prime Factorization Algorithm: %d",gcdPrimeFactorization(num1,num2));
return 0;
}
int gcdEuclid(int a,int b)
{
int temp;
while(b!=0){
temp=b;
b=a%b;
a=temp;
}
return a;
}
int gcdMiddleSchool(int a, int b){
while(a!=b)
{
if(a>b)
a-=b;
else
b-=a;
}
return a;
}
int gcdPrimeFactorization(int a, int b)
{
int gcd=1;
int factor=2;
while(a>1 && b>1)
{
if(a % factor == 0 && b % factor == 0)
{
gcd*=factor;
a/=factor;
b/=factor;
}
else if(a % factor ==0)
{
a/=factor;
}
else if(b % factor ==0)
{
b/=factor;
}
else
{
factor++;
}	
}	
return gcd;
}

