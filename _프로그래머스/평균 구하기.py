"""
* Title: 평균 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/12944
"""
def solution(arr):
    result = sum(arr)
    answer = result / int(len(arr))
    return answer