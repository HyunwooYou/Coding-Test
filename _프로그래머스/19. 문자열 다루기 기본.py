"""
* Title: 문자열 다루기 기본
https://school.programmers.co.kr/learn/courses/30/lessons/12918
"""
def solution(s):
    answer = True
    length = len(s)

    if not (length == 4 or length == 6):
        answer = False
    if i in range(0, length):
        num = ord(s[i]) - 48
        if num >= 10:
            answer = False

    return answer