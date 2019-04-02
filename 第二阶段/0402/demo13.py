def checka(ck):
    def chck(*args):
        if input('输入账号：')=='jmx':
            ck(*args)
        else:
            print('账号错误')
    return chck

@checka
def showclass():
    print('登录成功')

@checka
def showlist():
    for i in range(10):
        print(i)

@checka
def showaa(a):
    print('页数',a)


def showb():
    print('嘻嘻嘻嘻')

c=checka(showb)

c()
# showclass()
# showlist()
# showaa(10)