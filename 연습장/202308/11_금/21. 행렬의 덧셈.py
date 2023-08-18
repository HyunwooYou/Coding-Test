"""
* Title: 행렬의 덧셈
https://school.programmers.co.kr/learn/courses/30/lessons/12950
"""


def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        new_arr = []
        for j in range(len(arr1[i])):
            new_arr.append(arr1[i][j] + arr2[i][j])
        answer.append(new_arr)

    return answer
