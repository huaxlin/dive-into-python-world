Dynamic Linking

test_fib:

```shell
$ make
...
$
$ export LD_LIBRARY_PATH=`pwd`:$LD_LIBRARY_PATH
$ time ./test_fib 36
fib(36) => 14930352
./test_fib 36  0.10s user 0.00s system 98% cpu 0.104 total
```

Cython:

```shell
$ CFLAGS="-I`pwd`/src"  \
  LDFLAGS="-L`pwd`"     \
    python setup.py build_ext -i
```

Before we run the module, we also need to make sure that `lib{xxx}` is in the LD_LIBRARY_PATH environment variable, e.g. by setting:

```shell
$ export LD_LIBRARY_PATH=`pwd`:$LD_LIBRARY_PATH
$ export PYTHONPATH=.
$
$ time python -c 'from fibonacci import fib; print(fib(36))'
14930352
python -c 'from fibonacci import fib; print(fib(36))'  0.09s user 0.02s system 75% cpu 0.147 total
$
$ time python -c 'from fibonacci import fib; print(fib(43))'
433494437
python -c 'from fibonacci import fib; print(fib(43))'  2.33s user 0.03s system 98% cpu 2.386 total
```

```shell
$ python
>>> stmt = """
def fib(n):
  if n<2:
    return n
  return fib(n-2) + fib(n-1)

print(fib(%d))
"""
>>> from timeit import timeit
>>> timeit(stmt % 36, number=1)
14930352
3.1384832080000002
>>>
>>> timeit("from fibonacci import fib; print(fib(36))", number=1)
14930352
0.10655062499999701
>>>
```
