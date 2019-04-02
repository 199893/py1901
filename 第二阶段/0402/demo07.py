def fun():
    yield 1
    yield 2
    yield 3
    return 'hello'

f=fun()

for i in f:
    i+=0
    print(i)


# try:
#     print(next(f))
#     print(next(f))
#     print(next(f))
#     print(next(f))
# except StopIteration as e:
#     print(e,'++++')