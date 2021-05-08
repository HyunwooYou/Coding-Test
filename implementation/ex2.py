input_data = input()
x = int(input_data[1])
y = int(ord(input_data[0])) - int(ord('a')) + 1

result = 0
steps = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

for step in steps:
    next_x = x + step[0]
    next_y = y + step[1]
    if 1 <= next_x <= 8 and 1 <= next_y <= 8:
        result += 1

print(result)
