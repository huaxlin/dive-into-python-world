from pyfibonacci cimport cfibonacci


cpdef long fib(long ord):
    return cfibonacci.fib(ord)
