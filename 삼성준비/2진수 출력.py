# 2진수 출력
num = 10
for iv in range(2 ** num):
  binary_str = format(iv, f'0{num}b')
  print(binary_str)

