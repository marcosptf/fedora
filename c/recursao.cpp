
#include <iostream>

using namespace std;

void contador(int num, int count=0);

/** 
 * recursao, neste caso eh como se tivesse usando um for, pq a saida sera assim:
 * [marcosptf@localhost c]$ g++ -v -Wall -orecursao recursao.cpp 
 *
 * [marcosptf@localhost c]$ ./recursao
 * 0
 * 1
 * 2
 * 3
 * 4
 * 5
 * 6
 * 7
 * 8
 * 9
 * 10
 *
 * */
void contador(int num, int count) {
    cout << count << "\n";
    if (num > count ){
        contador(num, ++count);
    }
}

int main(){
    contador(10);
    return 0;
}


