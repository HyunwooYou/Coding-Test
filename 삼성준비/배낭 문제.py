def knapsack(n, weights, values, capacity):
  # dp[i][j]: i번째 물건까지 고려하여 가방 용량이 j일 때 얻을 수 있는 최대 가치
  dp = [[0] * (capacity + 1) for _ in range(n + 1)]

  for i in range(1, n + 1):
    for j in range(capacity + 1):
      # 현재 물건을 가방에 넣을 수 있는 경우와 넣지 않는 경우 중 더 큰 가치 선택
      if weights[i - 1] <= j:
        dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])
      else:
        dp[i][j] = dp[i - 1][j]

  for row in dp[1:]:
    print(row[1:])

  return dp[n][capacity]

# 테스트
n = 3
weights = [1, 2, 3]
values = [60, 100, 120]
capacity = 5

result = knapsack(n, weights, values, capacity)
print(result)  # 출력: 220
