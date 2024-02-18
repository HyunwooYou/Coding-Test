bn = 5  # 박스의 수
cw = 20  # 컨테이너의 최대 길이
box = [
  (2, 10),
  (2, 14),
  (4, 10),
  (6, 10),
  (17, 20),
]  # 박스의 크기, 회전 가능

d = [[0] * (cw + 1) for _ in range(bn + 1)]

for i in range(1, bn):
  for j in range(1, cw + 1):
    # 현재 박스를 포함하지 않는 경우
    d[i + 1][j] = d[i][j]
    for k in range(2):
      # 현재 박스를 포함하는 경우
      if box[i][k] <= j:
        d[i + 1][j] = max(d[i + 1][j], d[i][j - box[i][k]] + (box[i][1 - k] * box[i][k]))

print(d[bn][cw])
