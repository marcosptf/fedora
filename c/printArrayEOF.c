#include <stdio.h>
#define MAXLINE 1000

/*
this character ==> '\0' is null, it is the end of array
 */

int getlines(char line[], int maxline);
void copy(char to[], char from[]);

main(){
  int len, max=0;
  char line[MAXLINE], longest[MAXLINE];
  
  while((len=getlines(line, MAXLINE))>0) {
    if(len > max){
      max = len;
      copy(longest, line);
    }
  }
  
  if(max > 0 ){
    printf("%s", longest);
  }
  return;
}

int getlines(char s[], int lim){
  int c, i;
  
  for(i=0;i<lim-1 && (c=getchar())!=EOF && c!='\n';++i) {
    s[i] = c;
    if(c=='\n'){
      s[i] = c;++i;
    }
  }    
  s[i]='\0';
  return i;   
}

void copy(char to[], char from[]) {
  int i=0;
  while((to[i] = from[i])!='\0'){
    ++i;
  }
}

