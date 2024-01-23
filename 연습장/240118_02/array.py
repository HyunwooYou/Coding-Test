ls = [(1, 2), (3, 2), (5, 1)]
target = 1

filtered = list(filter(lambda x: x[1] == target, ls))
mapped = list(map(lambda x: x[0], ls))
sorted = sorted(ls, key=lambda x: x[0], reverse=True)

ls = [1, 2 ,3, 4]
print(ls[:-1])
print(ls[1:])
print(ls[-1])
