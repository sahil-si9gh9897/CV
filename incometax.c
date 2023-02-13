#include<stdio.h>

int main(){
float income;
float tax;

printf("Enter your annual income\n");
scanf("%f", &income);

if(income>=250000 && income<=500000){
    tax = tax + 0.05 * (income - 250000);
}
if(income>=500001 && income<=1000000){
    tax = tax + 0.1 * (income - 500001);
}
if(income>=1000001 ){
    tax = tax + 0.2 * (income - 1000001);
}
printf("your payable tax on your income is %f\n ", tax);





return 0;
}