"""
* Title: 최댓값과 최솟값
https://school.programmers.co.kr/learn/courses/30/lessons/12939
"""


def solution(s):
    strls = s.split()
    intls = []

    for i in range(0, len(strls)):
        intls.append(int(str[i]))
    intls.sort()
    min = str(intls[0])
    max = str(intls[len(intls) - 1])
    return min + ' ' + max
