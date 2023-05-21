from setuptools import Extension, setup
from Cython.Build import cythonize

setup(
    name='Hello world app',
    # ext_modules=cythonize([Extension("fibonacci", ["fibonacci.pyx"])]),
    ext_modules=cythonize([
        Extension("fibonacci", ["fibonacci.pyx"],  #       naive,        sequence computer
                  libraries=["fib"])  # libfib.so  # TODO: libfib.so.1, libfib.so.2
    ]),
    zip_safe=False,
)
