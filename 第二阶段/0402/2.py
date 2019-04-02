'''
2，新建2.py文件
创建列表，元组，字典，字符串，整形
判断以上类型是否可以迭代，是否是迭代器
如果是迭代器则使用next得到所有内容
'''
from collections.abc import Iterator,Iterable

a=[1,2,3]
b=(4,5,6)
c={7,8,9}
d="10,11,12"
e=13,14,15


#Iterable判断是否可以迭代
# Iterator判断是否是迭代器,可以使用next的都是迭代器
# 列表
print(isinstance(a,Iterable))
print(isinstance(a,Iterator))
# 元组
print(isinstance(b,Iterable))
print(isinstance(b,Iterator))
# 字典
print(isinstance(c,Iterable))
print(isinstance(c,Iterator))
# 字符串
print(isinstance(d,Iterable))
print(isinstance(d,Iterator))
# 整形
print(isinstance(e,Iterable))
print(isinstance(e,Iterator))