#include<stdio.h>

/*
this program has compiled with some warnings: 
!bash-4.2# gcc -o countingLinesInput countingLinesInput.c  
countingLinesInput.c: In function ‘main’:
countingLinesInput.c:7:9: warning: comparison between pointer and integer [enabled by default]
     if(c=="\n"){
         ^
         
i discovered why this warning, in clang, when the comparison is with double quotes, 
is string but with single quotes is integer expresion         

:-O

*/

main() {
  int c,n1=0;
  
  while((c = getchar()) != EOF) {
    if(c=='\n'){
      ++n1;
    }
    printf("%d\n",n1);
  }
  
}