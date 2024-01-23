'''
* 중복이 없는 경우 dict['a'].add
'''
from collections import defaultdict

dict = defaultdict(set)

dict[('a', 'aa')].add(('a_name', 0))
dict['b'].add(('b_name', 10))
dict['c'].add(('c_name', 20))

print(list(dict.get('b'))[0][0])
print(('a', 'aa') in dict)

for i in dict.items():
  cur = list(i[1])
  print(cur)

ls = [1, 2, 3, 4, 5]

print(''.join([str(i) for i in ls]))