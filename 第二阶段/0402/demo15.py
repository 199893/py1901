import time,datetime

class Ly():
    def __init__(self,fun):
        self.fun=fun
        print('这是第一步',datetime.datetime.now())
        time.sleep(1)
        self.fun()

    def __call__(self):
        print('这是第三步',datetime.datetime.now())
        time.sleep(1)


@Ly
def show():
    print('这是第二步',datetime.datetime.now())
    time.sleep(1)


show()

