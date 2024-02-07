bn = 8
cw = 26
box = [
  (17, 20),
  (6, 10),
  (4, 10),
  (14, 2),
  (2, 10),
  (8, 8),
  (10, 14),
  (14, 16),
]

def solution(bn, cw, box):
  dp = [[0] * (cw + 1) for _ in range(bn + 1)]

  for i in range(1, bn + 1):
    for j in range(cw + 1):
      dp[i][j] = dp[i - 1][j]
      for k in range(box[i - 1][0], min(j + 1, box[i - 1][1] + 1)):
        dp[i][j] = max(dp[i][j], dp[i - 1][j - k] + k * box[i - 1][0])

  return dp[bn][cw]

result = solution(bn, cw, box)
print(result)