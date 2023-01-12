def solution(arr):
    if (not (len(arr) > 1)):
        return [-1]
    arr.pop(arr.index(min(arr)))
    return arr