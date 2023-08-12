"""
* Title: 나누어 떨어지는 숫자 배열
https://school.programmers.co.kr/learn/courses/30/lessons/12910
"""
def solution(array, divisor):
    answer = []
    for i in array:
        if i % divisor == 0:
            answer.append(i)
    answer.sort()
    if int(len(answer)) == 0:
        return [-1]
    else:
        return answer