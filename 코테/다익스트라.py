"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

0
2
3
1
2
4
"""
from collections import deque

inf = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
d = [inf] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def bfs(start):
  q = deque()
  q.append((start, 0))
  d[start] = 0

  while q:
    cur, cur_dist = q.popleft()

    if d[cur] < cur_dist:
      continue

    for adj, adj_dist in graph[cur]:
      new_dist = cur_dist + adj_dist
      if new_dist < d[adj]:
        d[adj] = new_dist
        q.append((adj, new_dist))

bfs(start)

for i in range(1, n + 1):
  if d[i] == inf:
    print('infINITY')
  else:
    print(d[i])