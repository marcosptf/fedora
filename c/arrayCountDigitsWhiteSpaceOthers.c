#include<stdio.h>

main() {
  
  int c, i, nwhite=0, others=0, ndigit[10];
  
  for(i=0;i< 10;i++){ndigit[i]=0;}
  
  while((c = getchar()) != EOF) {
    
    if(c >= '0' && c <= 9) {
      ++ndigit[c-'0'];
    }else if(c==' ' || c == '\n' || c == '\t') {
      ++nwhite;
    }else{
      ++others;
    }      
  }
  
  printf("digits => ");
  for(i=0;i< 10;i++){
    printf(" %d", ndigit[i]);
  }
  printf(", white space => %d, other => %d \n", nwhite, others);
  
}
