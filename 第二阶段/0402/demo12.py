'''
检测到需要执行的函数selectgoods 拥有装饰器@checkaccess
不执行selectgoods 而是将selectgoods 作为参数传入checkaccess方法，
并且执行checkaccess 方法 此时sg =selectgoods
将checkaccess的执行结果返回，即将check方法的引用返回，即实际执行的是check方法

'''
def checkaccess(sg):
    def check():
        name=input('输入:')
        if name=='jmx':
            sg()
        else:
            print('没有权限')
    return check

@checkaccess
def selectgoods():
    print('开始查询')

selectgoods()