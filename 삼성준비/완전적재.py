import time
from itertools import combinations
from collections import defaultdict

start = time.time()


bn = 8
cw = 26
box = [
	(17, 20),
	(6, 10),
	(4, 10),
	(14, 2),
	(2, 10),
	(8, 8),
	(10, 14),
	(14, 16),
]


def binary_ls(num):
    str_ls = []
    for iv in range(2 ** num):
        str_ls.append(format(iv, f'0{num}b'))
    return str_ls


def solution(bn, cw, box):
    d = [0] * (100 + 1)

    for iv in range(1, bn + 1):
        # if dict.get(iv)
        if dict[iv] != None:
            dict[iv].extend(binary_ls(iv))

        for jv in combinations(box, iv):
            jv_ls = list(jv)

            for kv in dict[iv]:
                k_sum = 0
                k_width = 0

                for l, lv in enumerate(kv):
                    if lv == '1':
                        k_width += jv_ls[l][1]
                    else:
                        k_width += jv_ls[l][0]

                    if k_width > cw:
                        k_width = 0
                        break

                    k_sum += jv_ls[l][0] * jv_ls[l][1]

                if k_width == 0:
                    break

                d[k_width] = max(d[k_width], k_sum)

    for i, iv in enumerate(d):
        if iv != 0:
            print(f'{i} : {iv}')


dict = defaultdict(list)

solution(bn, cw, box)

print(time.time() - start)