#!/usr/bin/env python
import random
import time


MAX_NUM = 10000
LIST_COUNT = 1000
LOOP_COUNT = 1000

def data_generate():
    return [random.randint(1, MAX_NUM) for _ in range(LIST_COUNT)]

def quick_sort(data):
    if len(data) < 1:
        return data

    pivot = data[0]
    latest = len(data)
    left = []
    right = []

    for x in range(1, latest):
        if data[x] <= pivot:
            left.append(data[x])
        else:
            right.append(data[x])

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] + right



def quick_sort2(data, begin, end):
    pivot = select_pivot(data, begin, end)
    i = begin
    j = end - 1

    while True:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1

        if i >= j:
            break

        data[i], data[j] = data[j], data[i]
        i += 1
        j -= 1

    if i - begin >= 2:
        quick_sort2(data, begin, i-1)
    if end - j >= 2:
        quick_sort2(data, j+1, end)


def select_pivot(data, begin, end):
    center = (begin+end) // 2
    if data[begin] < data[center]:
        if data[center] < data[end-1]:
            return data[center]
        elif data[end-1] < data[begin]:
            return data[begin]
        return data[end-1]

    if data[end-1] < data[center]:
        return data[center]
    elif data[begin] < data[end-1]:
        return data[begin]
    return data[end-1]


if __name__ == '__main__':
    start = time.time()
    for _ in range(LOOP_COUNT):
        data = data_generate()
        quick_sort2(data, 0, len(data))

    end = time.time()
    print('経過時間:', (end-start))

    start = time.time()
    for _ in range(LOOP_COUNT):
        data = data_generate()
        sorted(data)

    end = time.time()
    print('経過時間:', (end-start))
