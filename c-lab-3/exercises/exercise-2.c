#include <stdio.h>

int main() {
    long *lPtr;
    long value1 = 200000;

    lPtr = &value1;
    printf("%ld\n", *lPtr);

    long value2 = *lPtr;
    printf("%ld\n", value2);
    printf("%p\n", (void *)&value1);
    printf("%p\n", (void *)lPtr);

    return 0;
}