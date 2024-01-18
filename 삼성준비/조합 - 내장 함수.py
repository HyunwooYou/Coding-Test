

from itertools import combinations

# 미리 계산된 조합을 저장할 딕셔너리
precomputed_combinations = {}

def get_combinations(n, r):
  # 먼저 딕셔너리에서 확인
  if (n, r) in precomputed_combinations:
    return precomputed_combinations[(n, r)]

  # 계산되지 않았다면 계산 후 딕셔너리에 저장
  result = list(combinations(range(n), r))

  precomputed_combinations[(n, r)] = result
  return result

# 예제 사용
print(get_combinations(40, 5))