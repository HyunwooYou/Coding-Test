from collections import deque

M = 3
ls = [1, 2, 3, 4]

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