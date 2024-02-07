'''
3
1 2 3
60 100 120
5

220
'''
n = int(input())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))
capacity = int(input())

# d[i][j]: i번째 물건까지 고려하여 가방 용량이 j일 때 얻을 수 있는 최대 가치
d = [[0] * (capacity + 1) for _ in range(n + 1)]

for i in range(n):
  for j in range(capacity + 1):
    # 현재 물건을 가방에 넣을 수 있는 경우와 넣지 않는 경우 중 더 큰 가치 선택
    if weights[i] <= j:
      d[i + 1][j] = max(d[i][j], values[i] + d[i][j - weights[i]])
    else:
      d[i + 1][j] = d[i][j]


print(d[n][capacity])
