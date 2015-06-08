#include<stdio.h>

int square(int num1){
    return num1 * num1;
}

int main(){
    int number,result;
    
    printf("\n Digite um numero");
    scanf("%d",&number);

    printf("O quadrado de %d eh:%d ",number,square(number));
    return(0);
}
