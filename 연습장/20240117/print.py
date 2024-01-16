"""
Hello, Coding Test!

Hello, Coding Test!
1 2 3 4
1 2 3 4
param-1 : param-2
"""
import sys

input_data = sys.stdin.readline().rstrip()

print(input_data)

ls = [1, 2, 3, 4]

print(' '.join(map(str, ls)))
print(*ls, sep=' ')

a = 'param-1'
b = 'param-2'

print(f"{a} : {b}")