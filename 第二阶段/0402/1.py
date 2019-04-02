'''
1，新建1.py文件
使用列表推导式构造生成器，使用next和for循环得到内容
使用yield得到函数式生成器，内部存储裴波拉契数列
如果函数return语句和yield关键字， 如何得到return的返回内容

'''


list=[i for i in range(5)]
list1=iter(list)
try:
    print(next(list1))
    print(next(list1))
    print(next(list1))
    print(next(list1))
    print(next(list1))
    print(next(list1))
except StopIteration:
    print('end')

# for i in list1:
#     print(i)



print("_______________________________")
#0,1,1,2,3,5,8
def fun(n):
    a=0
    b=1
    yield a
    yield b
    num=0
    while num<n:
        a,b=b,a+b
        yield b
        num+=1
f=fun(5)
for i in f:
    print(i)

print('__________________________________')

def fun1():
    yield 1
    yield 2
    yield 3
    return 'hello'

f1=fun1()

try:
    print(next(f1))
    print(next(f1))
    print(next(f1))
    print(next(f1))
except StopIteration as e:
    print(e,'++++')


