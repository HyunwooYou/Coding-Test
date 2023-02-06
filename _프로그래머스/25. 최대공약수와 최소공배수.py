"""
* Title: 최대공약수와 최소공배수
https://school.programmers.co.kr/learn/courses/30/lessons/12940
"""
def solution(n, m):
    num1 = greatest_common_divisor(n, m)
    num2 = least_common_multiple(n, m)

    return [num1, num2]

def greatest_common_divisor(x, y):
    while(y):
        x, y = y, x % y
    return x

def least_common_multiple(x, y):
    return (x * y) // greatest_common_divisor(x, y)