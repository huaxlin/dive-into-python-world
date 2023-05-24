"""
Mandelbrot set
==============

Compute the Mandelbrot fractal and plot it

"""
import matplotlib.pyplot as plt

def compute_mandelbrot(N_max, some_threshold, nx, ny):
    # A grid of c-values
    x = [i * (3.0 / (nx - 1)) - 2.0 for i in range(nx)]
    y = [i * (3.0 / (ny - 1)) - 1.5 for i in range(ny)]

    mandelbrot_set = [[0 for i in range(nx)] for j in range(ny)]

    for i in range(nx):
        for j in range(ny):
            c = complex(x[i], y[j])
            z = c

            for n in range(N_max):
                if abs(z) > some_threshold:
                    mandelbrot_set[j][i] = n
                    break
                z = z**2 + c

    return mandelbrot_set

mandelbrot_set = compute_mandelbrot(500, 500., 1601, 1401)

plt.imshow(mandelbrot_set, extent=[-2, 1, -1.5, 1.5])
plt.gray()

plt.savefig('mandelbrot_set.pure-python.png')
