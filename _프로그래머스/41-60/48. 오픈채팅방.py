"""
* Title: 오픈채팅방
"""
from collections import defaultdict

def solution(record):
    ans = []
    dict_users = defaultdict(str)

    for i in range(len(record)):
        cur = record[i]
        splitted = cur.split(' ')
        type = splitted[0]
        key = splitted[1]

        if type == 'Enter' or type == 'Leave':
            ans.append((key, type))

        if type == 'Enter' or type == 'Change':
            nickname = splitted[2]
            dict_users[key] = nickname

    for i in range(len(ans)):
        cur = ans[i]
        dynamic = ('나갔', '들어왔') [cur[1] == 'Enter']
        msg = '님이 ' + dynamic  + '습니다.'
        ans[i] = dict_users[cur[0]] + msg

    return ans

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))
