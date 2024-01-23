"""
* Title: 제일 작은 수 제거하기

* Input
4 3 2 1

* Output
4 3 2
"""
list = list(map(int, input().split()))


def solution(arr):
    if (not (len(arr) > 1)):
        return [-1]
    arr.pop(arr.index(min(arr)))
    return arr


solution(list)

print(list)
