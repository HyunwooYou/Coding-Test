"""
* Title: 카펫
https://school.programmers.co.kr/learn/courses/30/lessons/42842
"""
def solution(brown, yellow):
    store_x = 3
    store_y = 3

    for x in range(4, brown + 1):
        for y in range(3, x + 1):
            check_yellow = (x - 2) * (y - 2)
            if check_yellow == yellow and brown + yellow == x * y:
                store_x = x
                store_y = y
                break

    return [store_x, store_y]