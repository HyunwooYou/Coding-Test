"""
* Title: 튜플
https://school.programmers.co.kr/learn/courses/30/lessons/64065
"""
def solution(s):
    sliced_s = s[2 : len(s) - 2]
    splitted_s = sliced_s.split('},{')
    ls = []
    answer = []

    for i in range(len(splitted_s)):
        # '1, 2, 3'
        cur_str = splitted_s[i]
        # [1 2 3]
        num_ls = list(map(int, cur_str.split(',')))
        ls.append(num_ls)

    sorted_ls = sorted(ls, key=lambda x: (len(x)))

    for i in range(len(sorted_ls)):
        if i == 0:
            answer.append(sorted_ls[0][0])
        else:
            cur = sorted_ls[i]
            for j in range(len(answer)):
                cur.remove(answer[j])
            answer.append(cur[0])

    return answer  