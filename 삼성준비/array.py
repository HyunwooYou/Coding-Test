ls = [(1, 0), (2, 1), (3, 2), (5, 3), (0, 4)]
target = 1
filtered = list(filter(lambda x: x[1] == target, ls))
mapped = list(map(lambda x: x[0], ls))
sorted_ls = sorted(ls, key=lambda x: x[0], reverse=True)
set_ls = list(set(sorted_ls)) # 중복 제거

num_ls = [1, 2, 3, 4, 5]

num_ls = num_ls[:-1]
# [1, 2, 3, 4]

num_ls = num_ls[1:]
# [2, 3, 4]

last = num_ls[-1]
# 4

print(last)

# 숫자 문자열 리스트를 숫자 리스트로 변경
str_ls = ['1', '2', '3']
print(str_ls)
num_ls = [int(iv) for iv in str_ls]
print(num_ls)