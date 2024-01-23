"""
* Title: JadenCase 문자열 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12951
"""


def solution(s):
    s = s.split(' ')
    answer = []

    for i in range(len(s)):
        new_str = ''
        for j in range(len(s[i])):
            is_num = ord(s[i][j]) - 48
            # integer
            if (0 < is_num <= 9):
                new_str += s[i][j]
            # string
            elif j == 0:
                new_str += s[i][j].upper()
            else:
                new_str += s[i][j].lower()
        answer.append(new_str)

    return ' '.join(answer)
