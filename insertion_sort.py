#!/usr/bin/env python
import random
import time


MAX_NUM = 10000
LIST_COUNT = 1000
LOOP_COUNT = 10000

def data_generate():
    return [random.randint(1, MAX_NUM) for _ in range(LIST_COUNT)]


def insertion_sort(data):
    for i in range(1, len(data)):
        tmp = data[i]
        if data[i-1] > tmp:
            j = i
            while j > 0 and data[j-1] > tmp:
                j -= 1

            data[j] = tmp


def insertion_sort2(data):
    for pos in range(1, len(data)):
        ins = pos
        while ins >= 1 and data[ins-1] > a[ins]:
            tmp = a[ins-1]
            a[ins-1] = a[ins]
            a[ins] = tmp
            ins -= 1


