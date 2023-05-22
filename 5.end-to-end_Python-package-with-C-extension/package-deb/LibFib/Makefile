CFLAGS = -Wall -Werror


.PHONY: all clean

all: libfib.so

clean:
	rm -f libfib.so fibonacci.o

libfib.so: fibonacci.o
	gcc -o libfib.so fibonacci.o -shared
fibonacci.o: src/fibonacci.c
	gcc -fPIC -c src/fibonacci.c -o fibonacci.o


test_fib: test_fib.c libfib.so
	gcc $(CFLAGS) test_fib.c -L . -I./src -lfib -o test_fib
	# gcc $(CFLAGS) test_fib.c -lfib -o test_fib


install:
	install -D ./src/fibonacci.h ${DESTDIR}/usr/include/fibonacci.h
	install -D ./libfib.so ${DESTDIR}/usr/lib/libfib.so

uninstall:
	rm /usr/include/fibonacci.h
	rm /usr/lib/libfib.so
