"""
* Title: 멀리 뛰기
https://school.programmers.co.kr/learn/courses/30/lessons/12914
"""
import math


def solution(n):
    answer = 0
    d = [0] * (n + 1)
    count_two = n // 2

    for two in range(1, count_two + 1):
        one = n - two * 2
        total = one + two
        result = factorial(d, total) // (factorial(d, one) * factorial(d, two))
        answer += result

    answer += 1
    return answer % 1234567


def factorial(d, num):
    if d[num] == 0:
        d[num] = math.factorial(num)

    return d[num]
