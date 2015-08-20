#include<stdio.h>

/*
 * this program frompage 20 has been failed on compilation time, debug after
 * 
!bash-4.2# gcc -o characterCountingFor characterCountingFor.c 
/tmp/ccKSwjz0.o: In function `main':
characterCountingFor.c:(.text+0x1e): undefined reference to `getchat'
collect2: error: ld returned 1 exit status

 */

main() {
  double nc;
  for(nc=0;getchat()!=EOF;++nc)
    ;
      printf("%.0f\n",nc);
  
}