'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

19
16
'''

# 테스트 케이스 입력
for tc in range(int(input())):
	# 금광 정보 입력
	n, m = map(int, input().split())
	array = list(map(int, input().split()))

	# 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
	d = []
	index = 0
	for _ in range(n):
		d.append(array[index:index + m])
		index += m

	# 다이나믹 프로그래밍 진행
	for x in range(1, m):
		for y in range(n):
			# 왼쪽 위에서 오는 경우
			if y == 0:
				left_up = 0
			else:
				left_up = d[y - 1][x - 1]

			# 왼쪽 아래에서 오는 경우
			if y == n - 1:
				left_down = 0
			else:
				left_down = d[y + 1][x - 1]

			# 왼쪽에서 오는 경우
			left = d[y][x - 1]

			d[y][x] = d[y][x] + max(left_up, left_down, left)

	result = 0
	for y in range(n):
		result = max(result, d[y][m - 1])

	print(result)
