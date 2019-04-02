class Goods():
    def __init__(self,_addr):
        self.addr=_addr
        self.index=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index<len(self.addr):
            result=self.addr[self.index]

