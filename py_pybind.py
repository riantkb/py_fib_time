import time
import fib_library


if __name__ == "__main__":

    mintrials = 5

    lis = []
    for i in range(mintrials):
        t = time.time()
        f = fib_library.fib(35)
        t = time.time() - t
        lis.append(t)

    lis.sort()
    print(lis[0], lis[mintrials // 2], lis[-1])
