"""
Mandelbrot set
==============

Compute the Mandelbrot fractal and plot it

"""
import numpy as np
import matplotlib.pyplot as plt

from functools import wraps
from time import time


def timeit(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            end_ = end_ / 1000
            print(f"Elapsed time: {end_ if end_ > 0 else 0} s")
    return _time_it


@timeit
def compute_mandelbrot(N_max, some_threshold, nx, ny):
    # A grid of c-values
    x = [i * (3.0 / (nx - 1)) - 2.0 for i in range(nx)]
    y = [i * (3.0 / (ny - 1)) - 1.5 for i in range(ny)]

    mandelbrot_set = [[True for i in range(nx)] for j in range(ny)]

    for i in range(nx):
        for j in range(ny):
            c = complex(x[i], y[j])
            z = c

            for n in range(N_max):
                if abs(z) > some_threshold:
                    mandelbrot_set[j][i] = False
                    break
                z = z**2 + c

    return mandelbrot_set

# mandelbrot_set = compute_mandelbrot(500, 500., 5601, 5401)
mandelbrot_set = compute_mandelbrot(500, 500., 601, 401)

mandelbrot_set = np.array(mandelbrot_set)
plt.imshow(mandelbrot_set, extent=[-2, 1, -1.5, 1.5])
plt.gray()

plt.show()
# plt.savefig('mandelbrot_set.pure-python.png')
