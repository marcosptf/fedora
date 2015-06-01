#include <stdio.h>

int main(){
  int i,j,k;
  char string1[] = "10 20 30";
  sscanf(string1,"%d %d %d",&i, &j, &k);
  printf("valores lidos=>%d, %d, %d",i,j,k);
  return(0);
}