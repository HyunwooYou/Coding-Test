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
2 4 6
'''
import time
from itertools import combinations

n = int(input())
target = list(map(int, input().split()))
info_ls = []

for i in range(1, n + 1):
  ls = list(map(int, input().split()))
  ls.append(i)
  info_ls.append(ls)

min_cost = int(1e9)
idx_ls = []

start = time.time()
for iv in range(1, n + 1):
  for jv in combinations(info_ls, iv):
    j_sum_ls = [sum(x) for x in zip(*jv)]

    cond1 = target[0] <= j_sum_ls[0]
    cond2 = target[1] <= j_sum_ls[1]
    cond3 = target[2] <= j_sum_ls[2]
    cond4 = target[3] <= j_sum_ls[3]

    if cond1 and cond2 and cond3 and cond4:
      if min_cost >= j_sum_ls[4]:
        idx_ls = list(map(lambda x: x[5], jv))
        min_cost = j_sum_ls[4]


print(min_cost)
print(*sorted(idx_ls), end=' ')

print()
# print(time.time() - start)