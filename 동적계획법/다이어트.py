'''
6
100 70 90 10
30 55 10 8 100
60 10 10 2 70
10 80 50 0 50
40 30 30 8 60
60 10 70 2 120
20 70 50 4 4

134
2 4 6
'''
n = int(input())
mp, mf, ms, mv = list(map(int, input().split()))
array = [list(map(int, input().split())) for _ in range(n)]

# 최소 비용과 해당하는 식단들을 저장할 변수들
min_cost = int(1e9)
min_path = []

# 재귀적으로 모든 경우를 탐색하는 함수
def dfs(index, remaining, path):
	global min_cost, min_path

	# 모든 식재료 선택을 완료한 경우
	if index == n:
		# 남은 식재료가 없는 경우 => 식재료 최소 조건을 만족함
		if all(r == 0 for r in remaining):
			new_cost = sum(array[i][4] for i in path)
			if new_cost < min_cost:
				min_cost = new_cost
				min_path = path[:]
		return

	# 선택 안 함
	dfs(index + 1, remaining, path)

	# 현재 식재료 선택
	new_remaining = [max(0, remaining[i] - array[index][i]) for i in range(4)]
	dfs(index + 1, new_remaining, path + [index])


# 최소 비용을 찾기 위한 호출
dfs(0, [mp, mf, ms, mv], [])

# 결과 출력
print(min_cost)
print(*[i + 1 for i in min_path])
