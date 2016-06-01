#!/usr/local/bin/python3
"""
def a(b):
    return b ** 3


for _ in range(10000):
    print(a(10))
"""


class A:
    def __init__(self):
        self.count = 0

    def a(self, b):
        self.count += 1
        return b ** 3 + self.count

obj = A()
for _ in range(10000):
    print(obj.a(10))

