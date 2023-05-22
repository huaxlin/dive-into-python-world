install shared object(to shared library):

```shell
$ #### install
$ install -D LibFib/src/fibonacci.h /usr/local/include/fibonacci.h
$ install -D LibFib/libfib.so /usr/local/lib/libfib.so
$ 
$ #### remove
$ rm /usr/local/include/fibonacci.h
$ rm /usr/local/lib/libfib.so
```

```shell
$ python setup.py build_ext -i
$ ldd pyfibonacci/fibonacci.cpython-39-x86_64-linux-gnu.so
        linux-vdso.so.1 (0x00007ffd323b9000)
        libfib.so => not found
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f2320652000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f2320891000)
$ 
$ python -c 'from pyfibonacci import fib; print(fib(36))'
ImportError: libfib.so: cannot open shared object file: No such file or directory
```

SEE: https://levelup.gitconnected.com/how-to-use-libraries-in-linux-c-program-d907c8528f9c#3c55

```shell
$ cat /etc/ld.so.conf
include /etc/ld.so.conf.d/*.conf
$ ls /etc/ld.so.conf.d/
fakeroot-x86_64-linux-gnu.conf  libc.conf  x86_64-linux-gnu.conf
$ cat /etc/ld.so.conf.d/libc.conf
# libc default configuration
/usr/local/lib
$
```

action:

```shell
$ ldconfig -p |grep libfib.so
$
$ sudo ldconfig
$ ldconfig -p |grep libfib.so
        libfib.so (libc6,x86-64) => /usr/local/lib/libfib.so
$
$ ldd pyfibonacci/fibonacci.cpython-39-x86_64-linux-gnu.so
        linux-vdso.so.1 (0x00007fff2da6d000)
        libfib.so => /usr/local/lib/libfib.so (0x00007f2b6301a000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f2b62df2000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f2b63036000)
$
$ python -c 'from pyfibonacci import fib; print(fib(36))'
14930352
$ 
$ time python -c 'from pyfibonacci import fib; print(fib(42))'
267914296
python -c 'from pyfibonacci import fib; print(fib(42))'  2.34s user 0.03s system 100% cpu 2.367 total
$
```

install python package

```shell
$ cd /tmp
$ pip list|grep fib
$
$ python -c 'from pyfibonacci import fib; print(fib(36))'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'pyfibonacci'
$ 
$ cd <path>/<to>/PPA/pyfibonacci; python setup.py install; cd /tmp
$ pip list|grep fib
pyfibonacci 0.0.1
$ 
$ python -c 'from pyfibonacci import fib; print(fib(36))'
14930352
$
```
