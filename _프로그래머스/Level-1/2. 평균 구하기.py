"""
* Title: 평균 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/12944
"""
def solution(array):
    result = sum(array)
    answer = result / int(len(array))

    return answer