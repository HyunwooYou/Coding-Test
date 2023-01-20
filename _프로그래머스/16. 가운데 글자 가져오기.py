"""
* Title: 가운데 글자 가져오기
https://school.programmers.co.kr/learn/courses/30/lessons/12903
"""
def solution(s):
    answer = ''
    length = len(s)
    if (length % 2 == 0):
        answer = s[length//2 - 1] + s[length//2]
    else:
        answer = s[length//2]

    return answer