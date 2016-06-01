#!/usr/bin/env python
import time
import random

LOOP_COUNT = 10000000

def judge(player, computer):
    if player == 1 and computer == 1:
        return 0
    elif player == 1 and computer == 2:
        return 1
    elif player == 1 and computer == 3:
        return 2
    elif player == 2 and computer == 1:
        return 2
    elif player == 2 and computer == 2:
        return 0
    elif player == 2 and computer == 3:
        return 1
    elif player == 3 and computer == 1:
        return 1
    elif player == 3 and computer == 2:
        return 2
    elif player == 3 and computer == 3:
        return 0


def judge2(player, computer):
    if player == computer:
        return 0
    elif player == 1 and computer == 2 or\
            player == 2 and computer == 3 or\
            player == 3 and computer == 1:
                return 1
    else:
        return 2


def judge3(player, computer):
    return (player - computer + 3) % 3


judge_table = ((0,1,2),(2,0,1),(1,2,0))
def judge4(player, computer):
    global judge_table
    return judge_table[player-1][computer-1]


if __name__ == '__main__':
    print('if else 9パターン')
    start = time.time()
    for _ in range(LOOP_COUNT):
        judge(random.choice((1,2,3)),random.choice((1,2,3)))
    end = time.time()
    print('経過時間:', (end - start))

    print('if else 3パターン')
    start = time.time()
    for _ in range(LOOP_COUNT):
        judge2(random.choice((1,2,3)),random.choice((1,2,3)))
    end = time.time()
    print('経過時間:', (end - start))

    print('数式パターン')
    start = time.time()
    for _ in range(LOOP_COUNT):
        judge3(random.choice((1,2,3)),random.choice((1,2,3)))
    end = time.time()
    print('経過時間:', (end - start))

    print('配列(リスト)パターン')
    start = time.time()
    for _ in range(LOOP_COUNT):
        judge4(random.choice((1,2,3)),random.choice((1,2,3)))
    end = time.time()
    print('経過時間:', (end - start))


