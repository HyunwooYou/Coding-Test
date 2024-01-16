"""
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

57
"""
n, m = map(int, input().split())
graph = []
visited = [[0] * m for _ in range(n)]
r, c, d = map(int, input().split())

# 0: 북, 1: 동, 2: 남, 3:서
# 0 => 3 => 2 => 1 (반시계 방향)으로 돌아야한다.
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
  graph.append(list(map(int, input().split())))

visited[r][c] = 1
cnt = 1

while True:
  flag = 0

  for _ in range(4):
    nx = r + dx[(d + 3) % 4]
    ny = c + dy[(d + 3) % 4]
    d = (d + 3) % 4

    if graph[nx][ny] == 1 or visited[nx][ny] == 1:
      continue

    if 0 <= nx < n and 0 <= ny < m:
      visited[nx][ny] = 1
      cnt += 1
      flag = 1
      r, c = nx, ny
      break

  if flag == 0:
    if graph[r - dx[d]][c - dy[d]] == 1:
      print(cnt)
      break
    else:
      r, c = r - dx[d], c - dy[d]
