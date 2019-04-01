class Good():
    def __init__(self,_name):
        self.name=_name

    @property
    def gname(self):
        return self.name

    @gname.setter
    def gname(self,_name):
        self.name=_name


g1=Good('tra')
print(g1.name)
g1.name='greenter'
print(g1.name)