"""
* Title: 하샤드 수
https://school.programmers.co.kr/learn/courses/30/lessons/12947
"""


def solution(x):
    arr = list(str(x))
    sum = 0
    answer = True

    for i in range(len(arr)):
        sum += int(arr[i])

    if x % sum == 0:
        answer = True
    else:
        answer = False

    return answer
