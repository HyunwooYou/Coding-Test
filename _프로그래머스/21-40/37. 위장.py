"""
* Title: 위장
https://school.programmers.co.kr/learn/courses/30/lessons/42578
"""
from collections import defaultdict
from functools import reduce


def solution(clothes):
    dict = defaultdict(set)
    answer = []

    for i in range(len(clothes)):
        cur = clothes[i]
        dict[cur[1]].add(cur[0])

    for i in dict.items():
        type_count = len(list(i[1]))
        # add empty case (x)
        # ['x', 'a1', 'a2'], ['x', 'b1', 'b2', 'b3'..]
        answer.append(type_count + 1)

    # exclude all empty case
    return reduce(lambda x, y: x * y, answer) - 1
