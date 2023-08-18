"""
* Title: 행렬의 곱셈
https://school.programmers.co.kr/learn/courses/30/lessons/12949
"""


def solution(arr1, arr2):
    arr1_row_len = len(arr1)
    arr1_col_len = len(arr1[0])
    arr2_col_len = len(arr2[0])
    answer = [[0] * arr2_col_len for _ in range(arr1_row_len)]

    for i in range(arr1_row_len):
        for k in range(arr2_col_len):
            new_value = 0
            for j in range(arr1_col_len):
                new_value += arr1[i][j] * arr2[j][k]

            answer[i][k] = int(new_value)

    return answer
