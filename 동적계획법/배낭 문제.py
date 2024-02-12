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
w = int(input())

# d[i][j]: i번째 물건까지 고려하여 가방 용량이 j일 때 얻을 수 있는 최대 가치
d = [[0] * (w + 1) for _ in range(n + 1)]

for i in range(n):
  for j in range(w + 1): # 가방 용량
    # 현재 물건을 가방에 넣을 수 있는 경우
    if weights[i] <= j:
      # 가방에 넣지 않는 경우와 넣는 경우 중 큰 가치 선택
      d[i + 1][j] = max(d[i][j], d[i][j - weights[i]] + values[i])
    else:
      d[i + 1][j] = d[i][j]


for iv in d:
  print(iv)

print(d[n][w])

