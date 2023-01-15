"""
* Title: 제일 작은 수 제거하기
https://school.programmers.co.kr/learn/courses/30/lessons/12935
"""
def solution(arr):
    if (not (len(arr) > 1)):
        return [-1]
    arr.pop(arr.index(min(arr)))

    return arr
