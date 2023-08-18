"""
* Title: 체육복
https://school.programmers.co.kr/learn/courses/30/lessons/42862
"""


def solution(n, lost, reserve):
    ls = [1] * (n + 2)

    for i in range(len(lost)):
        cur = lost[i]
        ls[cur] -= 1

    for i in range(len(reserve)):
        cur = reserve[i]
        ls[cur] += 1

    for i in range(1, n + 1):
        cur = ls[i]

        if cur == 0 or cur == 1:
            continue
        if ls[i - 1] == 0:
            ls[i - 1] = 1
            ls[i] = 1
        if ls[i + 1] == 0:
            ls[i + 1] = 1
            ls[i] = 1
            continue
    ans = 0
    for i in range(1, n + 1):
        if ls[i] >= 1:
            ans += 1

    return ans


# n = 5
# lost = [2, 4]
# reserve = [1, 3, 5]

n = 5
lost = [2, 4]
reserve = [3]

print(solution(n, lost, reserve))
