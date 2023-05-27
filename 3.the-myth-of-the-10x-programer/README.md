- [ ] pidigits
- [ ] fasta
- [ ] spectral-norm
- [ ] n-body
- [x] mandelbrot


mandelbrot:

```shell
$ cd mandelbrot
$
$ python plot_mandelbrot_numpy.py
$ 
$ g++ -o mandelbrot_set mandelbrot_set.cpp
$ #### g++ -std=c++11 -o mandelbrot_set mandelbrot_set.cpp
$ ./mandelbrot_set
$ python plot_mandelbrot_set.py
$
$ python testing.py mandelbrot_set.numpy.png mandelbrot_set.cpp.png
Two image are almost equal.
```
