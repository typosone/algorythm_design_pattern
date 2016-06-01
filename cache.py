#!/usr/local/bin/python3
import time
import math
import sys

LOOP_COUNT = 100000000

a = 3;
b = 5;
c = -1;

print("キャッシュ無しバージョン")
start = time.time()
for _ in range(LOOP_COUNT):
    x1 = (-b + math.sqrt(b * b - 4 * 4 * a * c)) / (2 * a);
    x2 = (-b - math.sqrt(b * b - 4 * 4 * a * c)) / (2 * a);
    if _ % (LOOP_COUNT / 100) == LOOP_COUNT / 100 - 1 :
        print('.', end='')
        sys.stdout.flush()
end = time.time()
print()
print('経過時間:', (end-start))


print("キャッシュ有りバージョン")
start = time.time()
cache = math.sqrt(b * b - 4 * 4 * a * c)
for _ in range(LOOP_COUNT):
    x1 = (-b + cache) / (2 * a);
    x2 = (-b - cache) / (2 * a);
    if _ % (LOOP_COUNT / 100) == LOOP_COUNT / 100 - 1 :
        print('.', end='')
        sys.stdout.flush()
end = time.time()
print()
print('経過時間:', (end-start))


