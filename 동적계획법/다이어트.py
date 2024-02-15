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
mp, mf, ms, mv = list(map(int, input().split(' ')))
diets = [list(map(int, input().split(' '))) for _ in range(n)]

# 최소 비용과 해당하는 식단들을 저장할 변수들
min_cost = float('inf')
min_path = []

# 재귀적으로 모든 경우를 탐색하는 함수
def find_min_cost(idx, remaining, path):
	global min_cost, min_path

	# 모든 식재료에 대한 선택을 완료한 경우
	if idx == n:
		# 남은 식재료가 없는 경우
		if all(ingredient == 0 for ingredient in remaining):
			total_cost = sum(diets[i][4] for i in path)
			if total_cost < min_cost:
				min_cost = total_cost
				min_path = path[:]
		return

	# 현재 식재료를 선택하지 않는 경우
	find_min_cost(idx + 1, remaining, path)

	# 현재 식재료를 선택하는 경우
	new_remaining = [max(0, remaining[i] - diets[idx][i]) for i in range(4)]
	find_min_cost(idx + 1, new_remaining, path + [idx])

# 최소 비용을 찾기 위한 호출
find_min_cost(0, [mp, mf, ms, mv], [])

# 결과 출력
print(min_cost)
print(*[idx + 1 for idx in min_path])