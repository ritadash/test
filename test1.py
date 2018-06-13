# -*- coding: utf-8 -*-
from random import randint


def roll_dice(n=2):
    """
    摇色子
    :param n: 色子的个数
    :return: n颗色子点数之和sasfsfsfsfdsfsfsdssffsdfsfsfsjjjjjjjjjjjjjjjjjjjjjj
    """
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
