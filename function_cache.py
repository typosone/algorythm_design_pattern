#!/usr/local/bin/python3
counter = 0

def fact(num):
    global counter
    counter += 1

    if num == 0:
        return 1
    return num * fact(num - 1)


# ここからキャッシュバージョン
counter = 0
class Fact:
    def __init__(self):
        self.cache = {}

    def fact(self, num):
        global counter
        counter += 1

        if num == 0:
            self.cache[num] = 1
            return 1;
        
        if num in self.cache.keys():
            return self.cache[num]

        self.cache[num] = num * self.fact(num-1)
        return self.cache[num]


if __name__ == '__main__':
    obj = Fact()
    for n in range(11):
        print('{0}! = {1}'.format(n, obj.fact(n)))

    print('counter = ', counter)

