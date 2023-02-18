"""
* Title: 정수 내림차순으로 배치하기
https://school.programmers.co.kr/learn/courses/30/lessons/12933
"""
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)

    return int("".join(ls))