import time
from itertools import combinations
from collections import defaultdict

start = time.time()

# bn = 8
# cw = 26
# box = [
#   (17, 20),
#   (6, 10),
#   (4, 10),
#   (2, 14),
#   (2, 10),
#   (8, 8),
#   (10, 14),
#   (14, 16),
# ]

bn = 4
cw = 10
box = [
  (6, 10),
  (4, 10),
  (2, 14),
  (2, 8)
]

d = [[] for _ in range(101)]
dict = defaultdict(list)
key_ls = []

for iv in box:
  h = iv[0]
  w = iv[1]
  d[h].append(w)
  d[w].append(h)

for i, iv in enumerate(d):
  # set_ls = list(set(d[i]))
  d[i] = sorted(d[i], reverse=True)

for i, iv in enumerate(d):
  if len(iv) == 0:
    continue
  dict[i].extend(iv)
  key_ls.append(i)

max_val = 0

for jv in range(1, len(key_ls) + 1):
  for kv in combinations(key_ls, jv):
    total = 0
    if sum(kv) != cw:
      continue
    print(kv)

    for cv in kv:
      total += dict[cv][0] * cv
      max_val = max(max_val, total)

print()
# for iv in box:
#   print(iv)
# print()

for i, iv in dict.items():
  print(f'{i}: {iv}')
print()

print(f'max_val: {max_val}')

print()
print(time.time() - start)
