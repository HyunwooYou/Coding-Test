'''
2 15
2
3

5
'''
# 정수 N, M을 입력 받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
	array.append(int(input()))

INF = int(1e9)
# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [INF] * (m + 1)

d[0] = 0

# 다이나믹 프로그래밍
for i in range(n):  # i: 화폐 단위
	for j in range(array[i], m + 1):  # j: 금액
		if d[j - array[i]] != INF:  # 화폐 단위로 만들 수 있는 경우
			d[j] = min(d[j], d[j - array[i]] + 1)


# 계산된 결과 출력
if d[m] == INF:   # 최종적으로 M원을 만드는 방법이 없는 경우
	print(-1)
else:
	print(d[m])