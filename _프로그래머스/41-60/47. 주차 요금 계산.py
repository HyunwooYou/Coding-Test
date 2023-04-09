"""
* Title: 주차 요금 게산
https://school.programmers.co.kr/learn/courses/30/lessons/92341
"""
import math
from collections import defaultdict

def get_int_time(str_time):
    splitted = str_time.split(':')
    hours = int(splitted[0]) * 60
    minutes = int(splitted[1])

    return hours + minutes

def solution(fees, records):
    dict = defaultdict(list)
    dict_sum = defaultdict(list)

    for i in range(len(records)):
        cur = records[i]
        splitted = cur.split(' ')
        time = get_int_time(splitted[0])
        key = int(splitted[1])
        type = splitted[2]
        dict[key].append((time, type))

    for i in dict.items():
        key = i[0]
        cur = list(i[1])
        cur.sort()
        dict[key] = cur

        if cur[-1][1] == 'IN':
            dict[key].append((24 * 60 - 1, 'OUT'))

    for i in dict.items():
        key = i[0]
        cur = i[1]
        sum = 0
        sum_2 = 0

        for j in range(len(cur) // 2):
            in_val = cur[j * 2][0]
            out_val = cur[j * 2 + 1][0]
            sum += out_val - in_val

        base_time = fees[0]
        base_fee = fees[1]
        unit_time = fees[2]
        unit_fee = fees[3]

        if sum <= base_time:
            sum_2 = base_fee
        else:
            sum_2 = base_fee
            sum_2 += math.ceil((sum - base_time) / unit_time) * unit_fee

        dict_sum[key].append(sum_2)

    sorted_ls = sorted(dict_sum.items(), key=lambda x: x[0])
    mapped_ls = list(map(lambda x: x[1][0], sorted_ls))

    return mapped_ls

fees = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT"
]

# fees = [120, 0, 60, 591]
# records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

# fees = [120, 0, 60, 591]
# records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
print()
print(solution(fees, records))