#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main() 
{
    char input[255];
    
    printf("Enter a sentence, up to 255 characters:\n");
    scanf(" %[^\n]", input);

    char *token = strtok(input, " "); 
    while (token != NULL) {
        printf("%s  %zu\n", token, strlen(token));
        token = strtok(NULL, " ");
    }
    return 0;
}
