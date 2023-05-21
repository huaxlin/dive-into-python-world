#include <stdio.h>
#include <stdlib.h>  // for strtol
#include <errno.h>

//#include "fibonacci.h"
#include <fibonacci.h>


int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <order number>\n", argv[0]);
        return 1;
    }

    char *p;
    errno = 0; // not 'int errno', because the '#include' already defined it
    long ord = strtol(argv[1], &p, 10);
    if (*p != '\0' || errno != 0) {
        printf("convert input number %s to integer error!\n", argv[1]);
        return 1; // In main(), returning non-zero means failure
    }

    long ret = fib(ord);
    // TODO: check out scope
    printf("fib(%ld) => %ld\n", ord, ret);
    return 0;
}
