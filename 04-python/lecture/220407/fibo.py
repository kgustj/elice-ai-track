import time

n = 100
lst = [0 for _ in range(n+1)]


def fibo_topdown(n):
    if n == 1 or n == 2:
        return 1
    if lst[n]:
        return lst[n]
    lst[n] = fibo_topdown(n - 1) + fibo_topdown(n - 2)

    return lst[n]


def fibo(n):
    if n == 1 or n == 2:
        return 1

    return fibo(n - 1) + fibo(n - 2)


start1 = time.time()
print(fibo_topdown(10), (time.time() - start1) * 1000)
start2 = time.time()
print(fibo(10), (time.time() - start2) * 1000)
