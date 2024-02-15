def calc(n1, oper, n2):
	if oper == 0: # 더하기 (+)
		return n1 + n2
	elif oper == 1: # 빼기 (-)
		return n1 - n2
	elif oper == 2: # 곱하기 (*)
		return n1 * n2
	elif oper == 3: # 나누기 (/)
		if n1 == 0 or n2 == 0:
			return -1
		else:
			return n1 // n2


def solution(n, number):
	limit = 32000
	inf = 9
	nums = []
	d = [inf] * (limit + 1)
	q = [1]

	d[1] = 2
	d[n] = 1

	cnt = 1
	while True:
		num = int(''.join([str(n)] * cnt))
		if num > limit:
			break
		nums.append(num)
		q.append(num)
		d[num] = cnt
		cnt += 1

	if d[number] != inf:
		return d[number]

	while q:
		cur = q.pop(0)

		for num in nums:
			new_cnt = d[cur] + d[num]

			for oper in range(4):
				new_val = calc(cur, oper, num)

				if new_val == -1 or new_val > limit or new_val < 0:
					continue

				if new_cnt < d[new_val]:
					d[new_val] = new_cnt
					q.append(new_val)

	# d = d[1:65]
	# for i, iv in enumerate(d):
	# 	print(f'{i} : {iv}')

	if d[number] == inf:
		return -1
	else:
		return d[number]

# print(solution(5, 12))
print(solution(8, 53))