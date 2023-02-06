"""
* Title: N개의 최소공배수
https://school.programmers.co.kr/learn/courses/30/lessons/12953
"""
def solution(arr):
    lcm = arr[0]

    for i in range(1, len(arr)):
        lcm = least_common_multiple(lcm, arr[i])

    return lcm

def greatest_common_divisor(x, y):
    while(y):
        x, y = y, x % y
    return x

def least_common_multiple(x, y):
    return (x * y) // greatest_common_divisor(x, y)