"""
Hello World!

Hello World!
1 2 3 4
1 2 3 4
param-1 : param-2
"""
import sys

# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()

# 입력받은 문자열 그대로 출력
print(input_data)

ls = [1, 2, 3, 4]

print(*ls, sep=' ')
print(' '.join(map(str, ls)))

a = 'param-1'
b = 'param-2'

print(f"{a} : {b}")