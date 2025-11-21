#include <stdio.h>

int main() {
    int *zPtr = NULL;
    int *aPtr = NULL;
    void *sPtr = NULL;
    int number, i;

    int z[5] = {1,2,3,4,5};
    zPtr = z;
    zPtr = z;

    /* use a pointer to get the first value of array */
    number = zPtr[0];
    printf("%d", number);

    /* assign array element 2 (the value 3) to number */
    number = zPtr[2];
    printf("%d", number);

    /* print the entire array z */ 
    for (i=0; i <5; i++) {
        printf("%d", zPtr[i]);
    }

    return 0;
}
