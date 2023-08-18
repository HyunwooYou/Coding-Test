"""
* Title: 문자열 내림차순으로 배치하기
https://school.programmers.co.kr/learn/courses/30/lessons/12917
"""


def solution(s):
    ls = list(str(s))
    ls.sort(reverse=True)
    answer = ''.join(ls)

    return answer
