"""
* Title: 숫자 문자열과 영단어
https://school.programmers.co.kr/learn/courses/30/lessons/81301
"""


def solution(s):
    answer = []
    ls = list(s)
    tmp = ''

    for i in range(len(ls)):
        cur = ord(ls[i]) - 48

        if (0 <= cur <= 9):
            answer.append(ls[i])
            tmp = ''
        else:
            tmp += ls[i]

        cur_tmp = str_to_num(tmp)
        if cur_tmp != -1:
            answer.append(cur_tmp)
            tmp = ''


def str_to_num(key):
    return {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }.get(key, -1)
