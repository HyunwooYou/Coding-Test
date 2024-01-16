"""
8
1
2 3 8
1 7
1 4 5
3 5
3 4
7
2 6 8
1 7

1 2 3 8 7 4 5 6
"""
from collections import deque

n = int(input())
start = int(input())

graph = [[]]
visited = [False] * (n + 1)

for _ in range(n):
  graph.append(list(map(int, input().split())))

def bfs(start):
  q = deque()
  q.append(start)
  visited[start] = True

  while q:
    cur = q.popleft()
    print(cur, end=' ')

    for adj in graph[cur]:
      if not visited[adj]:
        q.append(adj)
        visited[adj] = True

bfs(start)