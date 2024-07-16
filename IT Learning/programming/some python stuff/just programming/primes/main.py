import time
import sys

def sieve(x, s):
    pri = []
    for i in range(2, s+1):
        if x[i]:
            for j in range(i*i, s+1, i):
                x[j] = False
    for i in range(2, s+1):
        if x[i]:
            pri.append(i+1)
    print((sys.getsizeof(x) + sys.getsizeof(pri)) / 1e6, 'MB')
    return pri


def trialdiv(x, s):
    for i in range(2, s+1):
        notprime = False
        for j in x:
            if j > i**0.5: break
            if i % j == 0:
                notprime = True
                break
        if not notprime: x.append(i)
    print(sys.getsizeof(x) / 1e6, 'MB')

if __name__ == '__main__':
    li = []
    n = 1000000
    t1 = time.time()
    trialdiv(li, n)
    print(time.time()-t1)
    print('There are', len(li), 'prime numbers in first', n, 'numbers')
    n = 100000000
    li = [True] * (n+1)
    t1 = time.time()
    primes = sieve(li, n)
    print(time.time()-t1)
    print('There are', len(primes), 'prime numbers in first', n, 'numbers')
