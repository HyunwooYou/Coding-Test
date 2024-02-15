'''
5
20
2 10
2 14
4 10
6 10
17 20

368
'''
n = int(input())
c = int(input())
box = []

d = [[0] * (c + 1) for _ in range(n + 1)]

for _ in range(n):
	a, b = map(int, input().split())
	box.append((a, b))

for i in range(n):
	for j in range(c + 1):
		# 현재 박스를 포함하지 않는 경우
		d[i + 1][j] = d[i][j]

		for k in range(2):
			# 현재 박스를 추가할 수 있는 경우
			if box[i][k] <= j:
				d[i + 1][j] = max(
					d[i + 1][j],
					d[i][j - box[i][k]] + (box[i][1 - k] * box[i][k])
				)

print(d[n][c])

