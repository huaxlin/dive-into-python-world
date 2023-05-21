#include "fibonacci.h"

long fib(long ord) {
    if (ord < 2) {
        return ord;
    }
    return fib(ord - 2) + fib(ord - 1);
}
