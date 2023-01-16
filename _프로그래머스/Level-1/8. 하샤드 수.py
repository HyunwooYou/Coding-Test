"""
* Title: 하샤드 수
https://school.programmers.co.kr/learn/courses/30/lessons/12947
"""
def solution(x):
    array = list(str(x))
    sum = 0
    answer = True

    for i in range(len(array)):
        sum += int(array[i])
        if x % sum == 0:
            answer = True
        else:
            answer = False

    return answer