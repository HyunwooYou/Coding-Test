'''
4
3 1 4 5
60 100 120 200 250
6

300
'''
n = int(input())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))
w = int(input())

d = [[0] * (w + 1) for _ in range(n + 1)]
s = [[[]] * (w + 1) for _ in range(n + 1)]

for i in range(n):
	for j in range(w + 1):
		if weights[i] <= j:
			if d[i][j] < d[i][j - weights[i]] + values[i]:
				d[i + 1][j] = d[i][j - weights[i]] + values[i]
				s[i + 1][j] = s[i][j - weights[i]] + [i]
			else:
				d[i + 1][j] = d[i][j]
				s[i + 1][j] = s[i][j]
		else:
			d[i + 1][j] = d[i][j]
			s[i + 1][j] = s[i][j]


print(d[n][w])