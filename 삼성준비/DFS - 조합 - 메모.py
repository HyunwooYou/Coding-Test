import time
from collections import deque

start = time.time()

M = 6
ls = list(range(1, 40))

def dfs_with_memo(comb: deque, depth: int, memo):
  if len(comb) == M:
    print(comb)
    return
  elif len(ls) == depth:
    return

  # 현재 상태를 튜플로 만들어 메모이제이션에 사용
  state = (tuple(comb), depth)
  if state in memo:
    # 이미 계산한 결과를 가져와서 중복 계산을 피함
    return

  comb.append(ls[depth])
  dfs_with_memo(comb, depth + 1, memo)

  comb.pop()
  dfs_with_memo(comb, depth + 1, memo)

  # 현재 상태의 결과를 메모이제이션
  memo.add(state)

def generate_combinations_with_memo():
  memo = set()
  dfs_with_memo(deque(), 0, memo)

# 테스트
generate_combinations_with_memo()
print(time.time() - start)