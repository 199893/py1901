'''
实例方法用来操作实例属性
类方法可以访问到类的内容
静态方法不可以访问类内容和实例内容

类与对象区别
类方法 静态方法 实例方法

'''
class Good():
    def __init__(self,_name):
        self.name=_name

    #声明类方法
    def getname(self):
        return self.name


    @staticmethod
    def dead():
        print('声明静态方法')

    @classmethod
    def printclass(cls):
        print('声明类方法')

a=Good('jmx')
# print(a.getname())

# print(a.dead())
# a.dead()
# Good.printclass()
