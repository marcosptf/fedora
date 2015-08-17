#include <stdio.h>

/*  print fahrenheit to celsius table */

main() {

  float fahr, celsius, lower, upper, step;
  
  lower = 0;
  upper = 300;
  step = 20;
  fahr = lower;
  
  printf("print integers numbers \n\n");
  
  while(fahr <= upper) {
    celsius = 5 * (fahr - 32.0) / 9;
    printf("%d\t%d\n", fahr, celsius);
    fahr+=step;
  }

  lower = 0;
  upper = 300;
  step = 20;
  fahr = lower;
  printf("print float numbers \n\n");
  while(fahr <= upper) {
    celsius = (5.0 / 9.0) * (fahr - 32.0);
    printf("%3.0f %6.1f \n", fahr, celsius);
    fahr+=step;
  }  
  
}
