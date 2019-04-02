'''
可迭代、迭代生成器
'''
from collections.abc import Iterator,Iterable
list=[1,2,3,4]
#Iterable判断是否可以迭代
# Iterator判断是否是迭代器,可以使用next的都是迭代器
print('<<<',isinstance(list,Iterable))
print('<<<',isinstance(list,Iterator))

print('^^^',isinstance({},Iterable))
print('^^^',isinstance({},Iterator))

print('>>>',isinstance((x for x in range(10)),Iterable))
print('>>>',isinstance((x for x in range(10)),Iterator))


#把 可迭代类型转换成迭代器
list1=iter(list)
print(next(list1))
print(isinstance(list1,Iterator))