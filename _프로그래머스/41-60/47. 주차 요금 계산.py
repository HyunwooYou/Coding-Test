"""
* Title: 주차 요금 게산
https://school.programmers.co.kr/learn/courses/30/lessons/92341
"""
import math
from collections import defaultdict
# math.ceil(12.34) => 13

def print_records(ls):
    for i in range(len(ls)):
        print(ls[i])
    print()

def get_int_time(str_time):
    splitted = str_time.split(':')
    hours = int(splitted[0]) * 60
    minutes = int(splitted[1])

    return hours + minutes

def solution(fees, records):
    answer = []
    base_time = fees[0]
    base_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    dict = defaultdict(set)


    print_records(records)

    for i in range(len(records)):
        cur = records[i]
        splitted = cur.split(' ')
        time = get_int_time(splitted[0])
        key = splitted[1]
        type = splitted[2]
        dict[key].add((time, type))

    for i in dict.items():
        cur = list(i[1])
        cur.sort()

        print(cur)

    return answer

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

solution(fees, records)