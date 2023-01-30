"""
* Title: 시저 암호
https://school.programmers.co.kr/learn/courses/30/lessons/12926
"""
def solution(s, n):
    new_ls = []

    for i in range(len(s)):
        ord_char = ord(s[i])
        moved = ord_char + n

        # space
        if ord_char == ord(' '):
            new_ls.append(' ')
        # lower char
        elif ord('a') <= ord_char <= ord('z'):
            if ord('a') <- moved <= ord('z'):
                new_ls.append(chr(moved))
            else:
                new_ls.append(chr(moved - 26))
        # upper char
        elif ord('A') <= ord_char <= ord('Z'):
            if ord('A') <= moved <= ord('Z'):
                new_ls.append(chr(moved))
            else:
                new_ls.append(chr(moved - 26))
        else:
            print('impossible case')

    return ''.join(new_ls)
