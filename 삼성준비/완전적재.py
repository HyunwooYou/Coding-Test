from collections import deque, defaultdict

bn = 8
cw = 26
box = [
  (17, 20),
  (6, 10),
  (4, 10),
  (14, 2),
  (2, 10),
  (8, 8),
  (10, 14),
  (14, 16),
]


def solution(bn, cw, box):
  d = [0] * (cw + 1)
  queue = deque([(0, 0, 0)])

  while queue:
    used, idx, sum_x = queue.popleft()

    for i in range(idx, bn):
      next_used = used | (1 << i)
      queue.append((next_used, i + 1, sum_x))

      k_sum = sum_x
      k_width = 0
      for l in range(bn):
        if (next_used >> l) & 1:
          k_width += box[l][1]
          k_sum += box[l][0] * box[l][1]

      if k_width <= cw:
        d[k_width] = max(d[k_width], k_sum)

  for i, iv in enumerate(d):
    if iv != 0:
      print(f'{i}: {iv}')
  return d[cw]


result = solution(bn, cw, box)

print(result)
