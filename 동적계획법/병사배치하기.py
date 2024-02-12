'''
7
15 11 4 8 5 2 4

2
'''
n = int(input())
ls = list(map(int, input().split()))
# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
ls.reverse()

# 다이나믹 프로그래밍을 위한 1차원 테이블 초기화
d = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
	for j in range(0, i):
		if ls[j] < ls[i]:
			d[i] = max(d[i], d[j] + 1)

# 열외해야 하는 병사의 최소 수를 출력
print(n - max(d))