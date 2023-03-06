"""
* Title: 타겟 넘버
https://school.programmers.co.kr/learn/courses/30/lessons/43165
"""
def solution(numbers, target):
    answer = 0
    types = ['0', '1']
    ls = [types[0], types[1]]

    count = 0
    while True:
        count += 1
        new_ls = []

        for i in range(len(ls)):
            for j in range(len(types)):
                new_ls.append(ls[i] + types[j])

        ls = new_ls
        if count == len(numbers) - 1:
            break

    for i in range(len(ls)):
        cur = ls[i]
        value = 0
        for j in range(len(cur)):
            # minus
            if cur[j] == '0':
                value += numbers[j] * (-1)
            # plus
            elif cur[j] == '1':
                value += numbers[j]
        if value == target:
            answer += 1

    return answer

# numbers = [1, 1, 1, 1, 1]
# target = 3

numbers = [4, 1, 2, 1]
target = 4

# 5
# 2
print(solution(numbers, target))