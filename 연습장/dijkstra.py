import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start):
  q = []
  heapq.heappush(q, (start, 0))
  distance[start] = 0

  while q:
    cur, cur_dist = heapq.heappop(q)

    if distance[cur] < cur_dist:
      continue

    for adj, adj_dist in graph[cur]:
      new_dist = cur_dist + adj_dist

      if new_dist < distance[adj]:
        distance[adj] = new_dist
        heapq.heappush(q, (adj, new_dist))


dijkstra(start)

for i in range(1, n + 1):
  if distance[i] == INF:
    print('INFINITY')
  else:
    print(distance[i])
