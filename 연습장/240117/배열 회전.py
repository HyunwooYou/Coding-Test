N = 5
board = [[i * N + j for j in range(N)] for i in range(N)]

def rotate45():
  new_board = [[0] * N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      new_board[i][j] = board[N - j - 1][i]

  return new_board

# before
for row in board:
  print(row)

# after
rotated = rotate45()

print()
for row in rotated:
  print(row);