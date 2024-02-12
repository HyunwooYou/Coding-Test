'''
4
1 3 1 5

8
'''

# 정수 N을 입력 받기
n = int(input())
# 모든 식량 정보 입력 받기
ls = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍 진행
d[0] = ls[0]
d[1] = max(ls[0], ls[1])

for i in range(2, n):
	d[i] = max(d[i - 1], d[i - 2] + ls[i])

# 계산된 결과 출력
print(d[n - 1])