/**
 * este eh o modulo c principal para ser usado como PyObject
 * precisa:
 * 1.criar o lab1.h
 * 2.compilar usando gcc para gerar uma lib => lab1.so
 * 3.codar a parte ctype python para importar estas functions
 * */

#include <math.h>

/* calcula o maximo divisor comum */
int gcd(int x, int y) {
    int g = y;
    while (x > 0){
        g = x;
	x = y % x;
	y = g;
    }
    return g;
}

/* testa se (x0,y0) esta ou n no conjunto de mandelbrot */
int in_mandel(double x0, double y0, int n) {
    double x=0, y=0, xtemp;
    while(n > 0){
        xtemp = x*x - y*y + x0;
	y = 2*x*y + y0
	x = xtemp;
	n -= 1;

	if (x*x + y*y > 4){
	    return 0;
	}
    }
    return 1;
}


/*  divide dois numeros */
int divide(int a, int b int *remainder){
    int quot = a / b;
    *remainder = a % b;
    return quot;
}

/* tira a media dos valores de um array  */
double avg(double *a, int n){
    int i;
    double total = 0.0;

    for(i=0, i < n; i++){
        total += a[i];
    }
    return total / n;
}

/* uma estrutura de dados em c */
typedef struct Point {
    double x, y;

} Point;

/* funcao que envolve uma estrutura de dados em c */
double distance(Point *p1, Point *p2) {
    return hypot(p1->x - p2->x, p1->y - p2->y);
}



