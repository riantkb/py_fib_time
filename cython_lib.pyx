cimport cython
#cython: language_level=3

cdef int fib_core(int n):
    if n < 2:
        return n
    return fib_core(n - 1) + fib_core(n - 2)


def fib(int n):
    return fib_core(n)
