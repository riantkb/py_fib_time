import time
import cython_lib


if __name__ == "__main__":

    mintrials = 5

    lis = []
    for i in range(mintrials):
        t = time.time()
        f = cython_lib.fib(35)
        t = time.time() - t
        lis.append(t)

    lis.sort()
    print(lis[0], lis[mintrials // 2], lis[-1])
