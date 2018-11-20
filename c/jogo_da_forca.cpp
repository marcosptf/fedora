/**
 * jogo da forca em cpp
 * g++ -v -Wall -ojogo_da_forca jogo_da_forca.cpp
 *
 */

#include <iostream>
#include <stdlib.h>

using namespace std;

int main() {

    char palavra[30], letra[1], secreta[30];
    int tam, i, chances, acertos;
    bool acerto=false;

    chances=6;
    tam=0;
    i=0;
    acerto=false;
    acertos=0;

    cout << "fala para seu amigo tampar os olhos e digite a palavra secreta=>";
    cin >> palavra;
    system("clear");

    while(palavra[i] != '\0') {
        i++; tam++;
    }

    for(i=0; i<30; i++){
        secreta[i]='-';
    }

    while((chances > 0) && (acertos < tam)) {
        cout << "chances restantes: " << chances << "\n\n";
	cout << "ṕalavra secreta: ";

	for(i=0; i<tam; i++){
	    cout << secreta[i];
	}

	cout << "\n\n digite uma letra: ";
	cin >> letra[0];

        for(i=0; i<tam; i++) {
	    if(palavra[i]==letra[0]) {
	        acerto=true;
	        secreta[i]=palavra[i];
	        acertos++;
	    }
        }

	if(!acerto) {
            chances--;
	}

	acerto=false;
	system("clear");
    }

    if(acertos==tam) {
        cout << "voce venceu \n\n";
    } else {
        cout << "vc perdeu \n\n";
    }
    
    return 0;
}



