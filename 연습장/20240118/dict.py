'''
* 중복이 없는 경우 dict['a'].add
'''
from collections import defaultdict

dict = defaultdict(set)

dict['a'].add(('a_name', 0))
dict['b'].add(('b_name', 10))
dict['c'].add(('c_name', 20))

print(list(dict.get('a'))[0][0])

for i in dict.items():
  cur = list(i[1])
  print(cur)