"""
* Title: 모의 고사
https://school.programmers.co.kr/learn/courses/30/lessons/42840
"""


def solution(answers):
    ls = answers
    p1 = [1, 2, 3, 4, 5]  # 5
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10
    ans = [0, 0, 0]
    ans2 = []

    for i in range(len(ls)):
        if ls[i] == p1[i % 5]:
            ans[0] += 1
        if ls[i] == p2[i % 8]:
            ans[1] += 1
        if ls[i] == p3[i % 10]:
            ans[2] += 1

    max_val = max(ans)
    for i, v in enumerate(ans):
        if v == max_val:
            ans2.append(i + 1)

    return ans2
