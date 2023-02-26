def solution(ls):
    print(ls)

    ls = [(1, 0), (2, 1), (3, 2), (5, 3), (0, 4)]
    target = 1
    filtered = list(filter(lambda x: x[1] == target, ls))
    sorted_ls = sorted(ls, key=lambda x: x[0], reverse=True)

