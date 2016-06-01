#!/usr/bin/env python
import time
import random

X = random.randint(3, 9)
LOOP_COUNT = 5000


def power(x, n):
    ans = 1
    for _ in range(n):
        ans *= x
    
    return ans


def power2(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x

    tmp = power2(x, n // 2)

    if n % 2 == 0:
        return tmp * tmp

    return tmp * tmp * x


def power3(x, n):
    ans = 1
    while n != 0:
        if n % 2 == 1:
            ans *= x

        n //= 2
        x *= x

    return ans


if __name__ == '__main__':
    print("単純なfor文のパターン")
    start = time.time()

    for n in range(10, LOOP_COUNT):
        power(X, n)

    end = time.time()
    print('経過時間:', (end-start))

    print('----')
    print("計算結果再利用パターン")
    start = time.time()

    for n in range(10, LOOP_COUNT):
        power2(X, n)

    end = time.time()
    print('経過時間:', (end-start))

    print('----')
    print("バイナリ法パターン")
    start = time.time()

    for n in range(10, LOOP_COUNT):
        power3(X, n)

    end = time.time()
    print('経過時間:', (end-start))



