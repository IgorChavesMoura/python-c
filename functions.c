
#include <stdio.h>

char* print_string(char* s){

	printf("%s no C\n",s);

	return s;
}

int hash (const char* word){
    
	unsigned int hash = 0;
    
	for (int i = 0 ; word[i] != '\0' ; i++){
        hash = 31*hash + word[i];
    }
    
	return hash;
}