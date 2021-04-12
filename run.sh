#!/bin/bash

echo cpp
./a.out

echo python
python py_python.py

echo pypy
pypy3 py_python.py

echo numba
python py_numba.py

echo pybind
python py_pybind.py

echo cython
python py_cython.py
