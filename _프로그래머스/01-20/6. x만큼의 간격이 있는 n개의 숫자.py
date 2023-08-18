"""
* Title: x만큼의 간격이 있는 n개의 숫자
https://school.programmers.co.kr/learn/courses/30/lessons/12954
"""


def solution(x, n):
    answer = []
    for i in range(1, n + 1):
        answer.append(i * x)

    return answer
