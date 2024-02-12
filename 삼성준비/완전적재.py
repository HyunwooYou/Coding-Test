# 주어진 파라미터: bn (박스의 수), cw (컨테이너의 폭), 그리고 박스의 크기
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

# 박스를 회전하여 얻을 수 있는 모든 경우를 포함한 상자 크기를 반환하는 함수
def get_rotated_boxes(box):
  rotated_boxes = []
  for w, h in box:
    rotated_boxes.append((w, h))
    if w != h:  # 회전할 수 있는 경우
      rotated_boxes.append((h, w))
  return rotated_boxes

# 회전한 상자를 얻음
rotated_box = get_rotated_boxes(box)

# 박스를 컨테이너에 담아 얻을 수 있는 최대 가치를 찾는 함수
def solution(bn, cw, box):
  # 최대 값들을 저장하기 위해 (bn+1) x (cw+1) 크기의 2차원 배열 dp를 초기화
  dp = [[0] * (cw + 1) for _ in range(bn + 1)]

  # 각 회전한 박스에 대해 반복
  for i in range(1, bn + 1):
    # 컨테이너의 가능한 폭에 대해 반복
    for j in range(cw + 1):
      # dp[i][j]를 이전 박스의 값으로 초기화
      dp[i][j] = dp[i - 1][j]
      # 현재 박스의 폭이 컨테이너에 맞는 범위 내에서 반복
      for k in range(rotated_box[i - 1][0], min(j + 1, rotated_box[i - 1][1] + 1)):
        # dp[i][j]를 현재 값과 현재 박스의 가치 * 폭을 더한 값 중 최대값으로 업데이트
        dp[i][j] = max(dp[i][j], dp[i - 1][j - k] + k * rotated_box[i - 1][0])

  # 모든 박스를 고려한 후 얻은 최대 값 반환
  return dp[bn][cw]

# solution 함수 호출하여 결과 출력
result = solution(bn, cw, rotated_box)
print(result)
