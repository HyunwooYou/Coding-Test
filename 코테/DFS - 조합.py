import time
from collections import deque

start = time.time()

M = 5
ls = list(range(1, 40))
answer = []

def dfs(comb: deque, depth: int):
  if len(comb) == M:
    # print(comb)
    answer.append(list(comb))
    return
  elif len(ls) == depth:
    return

  comb.append(ls[depth])
  dfs(comb, depth + 1)

  comb.pop()
  dfs(comb, depth + 1)

dfs(deque(), 0)

print(answer)

print(time.time() - start)