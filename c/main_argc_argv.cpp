#include <iostream>
#include <string.h>
#include <stdlib.h>

using namespace std;

int main(int argc, char *argv[]) {

	if (argc > 1) {
	    if (!strcmp(argv[1], "sol")) {
	    	cout << "esta sol vou ao clube \n\n";
	    } else if (!strcmp(argv[1], "nublado")) {
	    	cout << "esta nublado, vou ao cilema \n\n";
	    } else {
	    	cout << "vou ficar em casa \n\n";
	    }
	}

	return 0;
}

