from setuptools import Extension, find_namespace_packages, setup
from Cython.Build import cythonize

packages = find_namespace_packages(include=['pyfibonacci*'])
extensions = [
    Extension(
        "pyfibonacci.fibonacci",
        ["pyfibonacci/fibonacci.pyx"],  #       naive,       sequence computer
        libraries=["fib"]  # libfib.so  # TODO: libfib.so.1, libfib.so.2
    ),
]

compiler_directives = {"language_level": 3}
extensions = cythonize(extensions, compiler_directives=compiler_directives)

setup(
    name='pyfibonacci',
    version="0.0.1",
    packages=packages,
    package_data={'pyfibonacci': ['*.pxd', '*.pyx']},
    include_package_data=True,
    zip_safe=False,
    ext_modules=extensions,
)
