
#include <iostream>

using namespace std;

void soma(int n1, int n2);
void soma();

void soma(int n1, int n2) {
    int re;
    re = n1 + n2;
    cout << "\n soma de " << n1 << " com  " << n2  << " => " << re << "\n\n";
}

void soma() {
    int valor_a, valor_b, resp;
    valor_a = 4;
    valor_b = 5;
    resp = valor_a + valor_b;
    cout << "\n soma de " << valor_a << " com " << valor_b << " => " << resp << "\n\n";
}

int main(){

    soma(3, 7);
    soma();
    return 0;

}

