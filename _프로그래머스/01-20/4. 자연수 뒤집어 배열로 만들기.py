"""
* Title: 자연수 뒤집어 배열로 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12932
"""


def solution(n):
    array = list(str(n))
    array.reverse()
    answer = list(map(int, array))

    return answer
