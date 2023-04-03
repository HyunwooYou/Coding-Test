def solution(ls):
    print(ls)

    ls = [(1, 0), (2, 1), (3, 2), (5, 3), (0, 4)]
    target = 1
    filtered = list(filter(lambda x: x[1] == target, ls))
    sorted_ls = sorted(ls, key=lambda x: x[0], reverse=True)
    mapped = list(map(lambda x: x[0], ls))

    num_ls = [1, 2, 3, 4, 5]
    # [1, 2, 3, 4]
    num_ls = num_ls[:-1]
    # [2, 3, 4]
    num_ls = num_ls[1:]
    # 5
    last = num_ls[-1]


