"""
* Title: K번째 수
https://school.programmers.co.kr/learn/courses/30/lessons/42748
"""
def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        command = commands[i]
        new_ls = []
        start = command[0] - 1
        end = command[1]
        k = command[2] - 1

        for j in range(start, end):
            new_ls.append(array[j])
        new_ls.sort()
        answer.append(new_ls[k])

    return answer