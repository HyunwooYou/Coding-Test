"""
* Title: 기능 개발
https://school.programmers.co.kr/learn/courses/30/lessons/42586
"""


def solution(progresses, speeds):
    prog = progresses
    ans1 = []
    ans2 = []

    for i in range(len(prog)):
        days = 0

        while prog[i] < 100:
            days += 1
            prog[i] += speeds[i]

        for j in range(i + 1, len(prog)):
            prog[j] += days * speeds[j]

        ans1.append(days)

    count = 0
    ans1.append(100001)
    for i in range(len(ans1) - 1):
        count += 1
        if ans1[i + 1] != 0:
            ans2.append(count)
            count = 0

    return ans2
