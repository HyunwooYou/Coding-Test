"""
Hello, Coding Test!

Hello, Coding Test!
1 2 3 4
1 2 3 4
param-1 : param-2
"""
import sys

input_data = sys.stdin.readline().rstrip()

ls = [1, 2, 3, 4]

print(*ls, sep=' ')
print(' '.join(map(str, ls)))
param1 = 'param-1'
param2 = 'param-2'

print(f"{param1} : {param2}")