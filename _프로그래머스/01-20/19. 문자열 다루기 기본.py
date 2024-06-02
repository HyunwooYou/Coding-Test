"""
* Title: 문자열 다루기 기본
https://school.programmers.co.kr/learn/courses/30/lessons/12918
"""


def solution(s):
    length = len(s)

    if not (length == 4 or length == 6):
        return False
    for i in range(0, length):
        num = ord(s[i]) - 48
        if num >= 10:
            return False

    return True
