import time
from numba import jit, int32


@jit(int32(int32), nopython=True)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":

    mintrials = 5

    lis = []
    for i in range(mintrials):
        t = time.time()
        f = fib(35)
        t = time.time() - t
        lis.append(t)

    lis.sort()
    print(lis[0], lis[mintrials // 2], lis[-1])
