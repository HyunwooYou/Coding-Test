import time
from collections import deque

start = time.time()

M = 6
ls = list(range(1, 40))

def dfs(comb: deque, depth: int):
  if len(comb) == M:
    print(comb)
    return
  elif len(ls) == depth:
    return

  comb.append(ls[depth])
  dfs(comb, depth + 1)

  comb.pop()
  dfs(comb, depth + 1)

dfs(deque(), 0)

print(time.time() - start)