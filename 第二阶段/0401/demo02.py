class AI():
    '''
    AI类
    '''
    def __init__(self,_speed):
        self.speed=_speed

    #声明类方法run
    def run(self):
        print('run速度为%d' %self.speed)

    #声明静态方法
    @staticmethod
    def dead():
        print('AI死亡')

    #声明类方法
    @classmethod
    def printclassinfo(cls):
        print("类文档%s" %cls.__doc__)

a1 = AI(50)
a1.run()
# a1.dead()
# a1.printclassinfo()
# AI.dead()