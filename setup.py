from setuptools import setup
from Cython.Build import cythonize


setup(
    name='cython_lib',
    ext_modules=cythonize("cython_lib.pyx"),
    zip_safe=False,
)
