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
from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
visited = [[False] * (n + 1) for _ in range(m + 1)]
cnt = 1

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

for _ in range(n):
  graph.append(list(map(int, input().split())))

def bfs(x, y, d):
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  global cnt

  while q:
    x, y = q.popleft()
    back_step = True

    for _ in range(4):
      d = (d + 3) % 4
      nx = x + dx[d]
      ny = y + dy[d]

      if 0 < nx <= n and 0 < ny <= m:
        if not visited[nx][ny] and graph[nx][ny] == 0:
          q.append((nx, ny))
          visited[nx][ny] = True
          back_step = False
          cnt += 1
          break

    if back_step:
      x -= dx[d]
      y -= dy[d]
      if graph[x][y] == 0:
        q.append((x, y))
      else:
        print(cnt)
        break


bfs(r, c, d)