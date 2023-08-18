"""
* Title: K진수에서 소수 개수 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/92335
"""
# N진수에서 N진수로
import math


def n_to_n(n, q):
    num_str = ''

    while n > 0:
        n, mod = divmod(n, q)
        num_str += str(mod)

    return num_str[::-1]


def is_prime(num):
    sqrt_num = int(math.sqrt(num))
    is_prime_flag = True

    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            is_prime_flag = False
            break

    return is_prime_flag


def solution(n, k):
    answer = 0
    str_num = n_to_n(n, k)

    splitted = str_num.split('0')
    filtered = list(filter(lambda x: (x != '1' and len(x) != 0), splitted))
    mapped = list(map(lambda x: int(x), filtered))

    for i in range(len(mapped)):
        cur = mapped[i]
        if is_prime(cur):
            answer += 1

    return answer


n = 437674
k = 3

# n = 110011
# k = 10

print(solution(n, k))

# print(int('211', 10))
# print(n_to_n(n, 3))
