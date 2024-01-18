from collections import deque

M = 3
ls = [1, 2, 3, 4]
visited = [False] * len(ls)
result = []

def dfs(perm: deque):
  if len(perm) == M:
    result.append(list(perm))
    print(perm)
    return

  for i, val in enumerate(ls):
    if visited[i]:
      continue

    perm.append(val)
    visited[i] = True
    dfs(perm)

    perm.pop()
    visited[i] = False

dfs(deque())
