#include <stdio.h>

int main(){
  int i;
  char string1[30];
  printf("entre um valor inteiro=>");
  scanf("%d",&i);
  sprintf(string1,"valor de i=>%d",i);
  puts(string1);
  return(0);
}