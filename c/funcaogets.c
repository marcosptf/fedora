#include <stdio.h>

int main(){
    char buffer[10];
    printf("entre com o seu nome:");
    gets(buffer);
    printf("o nome eh:%s",buffer);
    return(0);
}