"""
* Title: 이중우선순위큐
https://school.programmers.co.kr/learn/courses/30/lessons/42628
"""


def solution(operations):
    ls = []

    for i in range(len(operations)):
        cur = operations[i].split(' ')
        if cur[0] == 'I':
            ls.append(int(cur[1]))
            ls = sorted(ls)
        elif len(ls) == 0:
            continue
        elif cur[0] == 'D' and cur[1] == '1':
            ls = ls[:-1]
        elif cur[0] == 'D' and cur[1] == '-1':
            ls = ls[1:]

    if len(ls) == 0:
        return [0, 0]
    else:
        min_val = max(ls)
        max_val = min(ls)
        return [min_val, max_val]


# operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

# [0, 0]
# [333, -45]
print(solution(operations))
