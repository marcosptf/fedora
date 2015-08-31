#include <stdio.h>

/** this function was compiled but with this warning ===>
!bash-4.2# gcc -o powerFunction powerFunction.c -std=c99
powerFunction.c:7:1: warning: return type defaults to ‘int’ [enabled by default]
 main(){
 ^
*/

//its is strange to my, but look like that the compiler c need a 
//signature of function before the use like this ==>
int power(int m, int n);

main(){
  
  for(int i=0;i<=10;i++){
    printf("%d %d %d\n", i, power(2,i), power(-3,i));
  }
  return 0;
}

int power(int base, int n){
  int i, p=1;
  for(int i=1;i<=n;i++){
    p = p * base;
    return base;
  }  
}

