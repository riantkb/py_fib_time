#!/bin/bash

# echo cpp
g++-10 -std=c++17 -O2 -Wall cpp.cpp

# echo python

# echo pypy

# echo numba

# echo pybind
g++-10 -O3 -Wall -shared -std=c++17 -fPIC `python3 -m pybind11 --includes` -undefined dynamic_lookup -o fib_library`python3-config --extension-suffix` fib_library.cpp

# echo cython
python setup.py build_ext --inplace
