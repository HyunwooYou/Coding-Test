"""
* Title: 핸드폰 번호 가리기
https://school.programmers.co.kr/learn/courses/30/lessons/12948
"""
def solution(phone_number):
    length = len(phone_number)
    back = phone_number[-4:]
    answer = '*' * (length - 4) + back

    return answer