"""
5 6
101010
111111
000001
111111
111111

10
"""
from collections import deque

n, m = map(int, input().split())
graph = []
visited = [[False] * (n + 1) for _ in range(m + 1)]

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

for _ in range(n):
  graph.append(list(map(int, input())))

def out_of_range(x, y):
  return x < 0 or y < 0 or x >= n or y >= m

def bfs(x, y):
  q = deque()
  q.append((x, y))
  visited[x][y] = True

  while q:
    x, y = q.popleft()

    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]

      if out_of_range(nx, ny) or visited[nx][ny]:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx, ny))

  return graph[n - 1][m - 1]

print(bfs(0, 0))