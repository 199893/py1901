'''
动态添加类属性
'''


class AI():
    #限制添加内容
    __slots__ = ('hp', 'mp',)

    def __init__(self,_hp):
        self.hp=_hp

#通过类名添加类属性
a1=AI(50)
print(a1.hp)
AI.isalive='jmx'
print(AI.isalive)
print(a1.isalive)

#通过实例名添加实例属性
a1.mp=80
print(a1.mp)

