'''
印裴波拉契算法
'''
#0,1,1,2,3,5,8
def fun(n):
    a=0
    b=1
    yield a
    yield b
    sum=0
    while sum<n:
        a,b=b,a+b
        yield b
        sum+=1

f=fun(5)
for i in f:
    print(i)