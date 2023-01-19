"""
* Title: 수박수박수박수
https://school.programmers.co.kr/learn/courses/30/lessons/12922
"""
def solution(n):
    answer = ('수박' * (n//2))
    if n % 2 == 1:
        answer += '수'

    return answer