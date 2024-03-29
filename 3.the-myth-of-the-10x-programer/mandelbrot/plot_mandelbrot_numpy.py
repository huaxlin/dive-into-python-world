"""
Mandelbrot set
==============

Compute the Mandelbrot fractal and plot it

"""
import numpy as np
import matplotlib.pyplot as plt
from numpy import newaxis

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
    x = np.linspace(-2, 1, nx)
    y = np.linspace(-1.5, 1.5, ny)

    c = x[:,newaxis] + 1j*y[newaxis,:]

    # Mandelbrot iteration

    z = c

    # The code below overflows in many regions of the x-y grid, suppress
    # warnings temporarily
    with np.warnings.catch_warnings():
        np.warnings.simplefilter("ignore")
        for j in range(N_max):
            z = z**2 + c
        mandelbrot_set = (abs(z) < some_threshold)

    return mandelbrot_set


# mandelbrot_set = compute_mandelbrot(500, 500., 5601, 5401)
mandelbrot_set = compute_mandelbrot(500, 500., 601, 401)

plt.imshow(mandelbrot_set.T, extent=[-2, 1, -1.5, 1.5])
plt.gray()

plt.show()
# plt.savefig('mandelbrot_set.numpy.png')
