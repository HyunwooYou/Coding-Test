"""
* Title: 실패율
https://school.programmers.co.kr/learn/courses/30/lessons/42889
"""


def solution(N, stages):
    ls = [0] * (N + 2)
    ans = []
    total = len(stages)

    for i in range(total):
        cur = stages[i]
        ls[cur] += 1

    for i in range(1, N + 1):
        cur = ls[i]
        if cur == 0:
            ans.append((i, 0))
            continue
        percent = cur / total
        ans.append((i, percent))
        total -= cur

    ans2 = sorted(ans, key=lambda x: x[1], reverse=True)
    ans3 = list(map(lambda x: x[0], ans2))

    return ans3


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

# N = 4
# stages = [4,4,4,4,4]

# [3,4,2,1,5]
# [4,1,2,3]
print(solution(N, stages))
