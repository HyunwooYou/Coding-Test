"""
* Title: 2016년
https://school.programmers.co.kr/learn/courses/30/lessons/12901
"""


def solution(a, b):
    days = 0

    for i in range(1, a):
        days += int(month_count(i))
    days += b

    return map_to_str((days - 1) % 7)


def month_count(key):
    return {
        1: '31',
        2: '29',
        3: '31',
        4: '30',
        5: '31',
        6: '30',
        7: '31',
        8: '31',
        9: '30',
        10: '31',
        11: '30',
        12: '31',
    }.get(key, -1)


def map_to_str(index):
    return {
        0: 'FRI',
        1: 'SAT',
        2: 'SUN',
        3: 'MON',
        4: 'TUE',
        5: 'WED',
        6: 'THU'
    }.get(index, -1)
