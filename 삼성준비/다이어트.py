'''
6
100 70 90 10
30 55 10 8 100
60 10 10 2 70
10 80 50 0 50
40 30 30 8 60
60 10 70 2 120
20 70 50 4 4

134
1 3 5
'''
from collections import deque

n = int(input())
mp, mf, ms, mv = list(map(int, input().split(' ')))
diets = [list(map(int, input().split(' '))) for _ in range(n)]

cost_min = float('inf')
costs = []


def bfs():
  global cost_min, costs
  q = deque([(0, [mp, mf, ms, mv], [])])

  while q:
    idx, remaining, path = q.popleft()
    # print(f'q: {q}')

    sum_x = sum([diets[i][4] for i in path])

    if sum(remaining) == 0:
      if sum_x < cost_min:
        costs = path
      cost_min = min(sum_x, cost_min)
      continue

    if len(path) == n:
      continue

    if sum_x > cost_min:
      continue

    for i in range(n):
      if i not in path:
        new_remaining = [max(0, y - x) for x, y in zip(diets[i], remaining)]
        new_path = path + [i]
        q.append((i + 1, new_remaining, new_path))


bfs()

print(cost_min)
for x in costs:
  print(x, end=' ')
