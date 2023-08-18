"""
* Title: H-Index
https://school.programmers.co.kr/learn/courses/30/lessons/42747
"""


def solution(citations):
    ls = citations
    answer = 0
    ls.sort()
    ls_len = len(ls)

    for i in range(ls_len):
        h = ls_len - i
        if ls[i] >= h:
            answer = h
            break

    return answer
