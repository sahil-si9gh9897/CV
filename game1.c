#include<stdio.h>
#include<stdlib.h>
#include<time.h>
// #include<math.h>

int main(){
int number , guess , nguesses=1;
srand(time(0));
number = rand()%100 +1;//this generates the number under 100
// printf("the random number is %d\n", number);
// keep running the program until the no. is guessed
// we ar using here loops
printf("****:NUMBER GUESSING GAME:****\n\n");
do{
printf("Guess the no. between 1 to 100\n");
scanf("%d", &guess);

if(guess>number){
    printf("\nplease choose  lower number try again:)\n\n");
}
else if(guess<number){
printf("\nplease choose a higher number try again:)\n\n");
}
else{
    printf("\nyou guessed it in %d attempts\n",nguesses);
}
nguesses++;
}
while(guess!=number);
return 0;
}