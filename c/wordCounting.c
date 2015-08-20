#include<stdio.h>

/*
 this program must have count lines, words and charactes in word

!bash-4.2# touch wordCounting.c
!bash-4.2# gcc -o wordCounting wordCounting.c
wordCounting.c: In function ‘main’:
wordCounting.c:21:30: error: lvalue required as left operand of assignment
     if(c==' ' || c=='\n' || c='\t') {
                              ^ 
 
 */

#define IN  1 /* inside a word */
#define OUT 2 /* outside a word */

main() {
  int c, n1=0, nw=0, nc=0, state=OUT;
  
  while((c = getchar()) != EOF) {
    ++nc;
    
    if(c=='\n') {
      ++n1;
    }
    
    if(c==' ' || c=='\n' || c=='\t') {
      state = OUT;
    } else if (state == OUT) {
      state = IN;
      ++nw;
    }
  }
  printf("%d %d %d\n", n1, nw, nc);
}

