'''
3，新建3.py文件
实现装饰器
功能为给现有的业务逻辑添加权限验证功能
或者实现统计时间消耗装饰器
要求：给与代码详细注释
'''
#导入时间模块
import time

# 闭个包
def timecount(f):
    def tc():
        start=time.time()
        f()
        end=time.time()
        print('消耗时间：',end-start)
    return tc

#创建装饰器，函数
@timecount
def listtime():
    list1=[i for i in range(100000)]
    print(list1.index(99999))


#创建装饰器，函数
@timecount
def getfromgeberator():
    g1=(x for x in range(100000))
    index=0
    while True:
        try:
            result=next(g1)
            if result==99999:
                print(index)
                break
            index += 1


        except StopIteration as e:
            print('没有找到')

#创建装饰器，函数
@timecount
def get1():
    g1=(i for i in range(100000))
    index=0
    for i in g1:
        index+=1
        if i==99999:
            print(i)

listtime()
getfromgeberator()
get1()
'''
系统解释到需要执行的函数listtime()拥有装饰器@timecount然后
不执行listtime(),将listtime()作为参数传入timecount(f)
执行timecount(f)，此时f=listtime()，return tc就是执行tc()
函数最后返回tc()方法的执行结果
'''