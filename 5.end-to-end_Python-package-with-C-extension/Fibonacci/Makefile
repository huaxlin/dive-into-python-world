FLAGS =

.PHONY: all clean

all: test_fib

clean:
	rm -f libfib.so fibonacci.o test_fib

fibonacci.o: src/fibonacci.c
	gcc -fPIC -c src/fibonacci.c -o fibonacci.o
libfib.so: fibonacci.o
	gcc -o libfib.so fibonacci.o -shared

test_fib: test_fib.c libfib.so
	gcc $(FLAGS) test_fib.c -L . -I./src -lfib -o test_fib
