def solution(array):
    if (not (len(array) > 1)):
        return [-1]
    array.pop(array.index(min(array)))

    return array
