"""
* Title: 프린터
https://school.programmers.co.kr/learn/courses/30/lessons/42587
"""


def solution(priorities, location):
    ls = []
    ans = []
    ans2 = 0

    for i in range(len(priorities)):
        # tuple: (value, index)
        ls.append((priorities[i], i))

    i = 0
    while True:
        if len(ls) == 0:
            break
        i += 1

        max_tuple = max(ls, key=lambda x: x[0])
        popped = ls.pop(0)

        if max_tuple[0] == popped[0]:
            ans.append(popped)
        else:
            ls.append(popped)

    for i in range(len(ans)):
        if ans[i][1] == location:
            ans2 = i + 1
            break

    return ans2


# priorities = [2, 1, 3, 2]
# location = 2
priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))
