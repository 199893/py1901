'''
动态添加实例方法
'''
import types
class AI():
    def __init__(self):
        pass


#定义实例方法
def move(self):
    print('move')

#重新定义变量名
a1=AI()
a1.move=types.MethodType(move,AI)#将封装的方法添加进class AI
a1.move()


#动态添加类方法，静态方法
#定义类方法
@classmethod
def attack(cls):
    print('attack')

# 定义静态方法
@staticmethod
def dead():
    print('dead')


AI.attack=attack
AI.attack()

AI.dead=dead
AI.dead()

#动态的删除属性，方法
# del a1.move
# a1.move()
