N = 5
board = [[0] * N for _ in range(N)]

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def init_grid():
  x = y = int(N / 2)
  direction = move_count = number = 0
  dist = 1

  while True:
    move_count += 1

    for _ in range(dist):
      nx = x + dx[direction]
      ny = y + dy[direction]

      if (nx, ny) == (-1, 0):
        return

      number += 1
      board[nx][ny] = number

      x = nx
      y = ny

    if move_count == 2:
      dist += 1
      move_count = 0

    direction = (direction + 1) % 4

init_grid()

for row in board:
  print(row)

