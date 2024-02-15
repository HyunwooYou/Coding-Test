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

# d[i][j]: i번째 물건까지 고려하여 가방 용량이 j일 때 얻을 수 있는 최대 가치
d = [[0] * (w + 1) for _ in range(n + 1)]
s = [[[]] * (w + 1) for _ in range(n + 1)]

for i in range(n):
  for j in range(w + 1):  # 가방 용량
    d[i + 1][j] = d[i][j]
    s[i + 1][j] = s[i][j]

    # 현재 물건을 가방에 넣을 수 있는 경우
    if weights[i] <= j:
      if d[i][j] < d[i][j - weights[i]] + values[i]:
        d[i + 1][j] = d[i][j - weights[i]] + values[i]
        s[i + 1][j] = s[i][j - weights[i]] + [i]  # Save the indices of items included


print(d[n][w])  # Print the maximum value
