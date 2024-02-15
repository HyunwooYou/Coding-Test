'''
2 15
2
3

5
'''
# 정수 N, M을 입력 받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력받기
ls = []
for i in range(n):
	ls.append(int(input()))

INF = int(1e9)
# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [INF] * (m + 1)

d[0] = 0

# 다이나믹 프로그래밍
for i in range(n):
	# j : 금액
	for j in range(ls[i], m + 1):
		# 화폐 단위로 만들 수 있는 경우
		if d[j - ls[i]] != INF:
			d[j] = min(d[j], d[j - ls[i]] + 1)

# 최종적으로 M원을 만드는 방법이 없는 경우
if d[m] == INF:
	print(-1)
# 계산된 결과 출력
else:
	print(d[m])