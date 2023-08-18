"""
* Title: 숫자 카드 게임-반복문
refer) 숫자 카드 게임

* Input
3 3
3 1 2
4 1 4
2 2 2

* Output
2
"""
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)  # 최종 답안 출력
