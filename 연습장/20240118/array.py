ls = [(2, 5), (3, 2), (5, 3)]
target = 1

filtered = list(filter(lambda x: x[1] == target, ls))
mapped = list(map(lambda x: x[0], ls))
sorted_ls = sorted(ls, key=lambda x: x[0], reverse=True)

ls = [1, 2, 3, 4, 5]

ls = ls[:-1]
print(ls)
ls = ls[1:]
print(ls)
ls = ls[-1]
print(ls)