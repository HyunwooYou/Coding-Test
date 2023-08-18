"""
* Title: 이상한 문자 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12930
"""


def solution(s):
    answer = []
    ls = s.split(' ')

    for i in range(len(ls)):
        str = ls[i]
        str_ls = list(str)

        for j in range(len(str_ls)):
            if (j % 2 == 0):
                str_ls[j] = str_ls[j].upper()
            else:
                str_ls[j] = str_ls[j].lower()
        answer.append(''.join(str_ls))

    return ' '.join(answer)
