
def gen():
    print('Generator start....')
    for i in range(0, 100):
        print('Before yield....')
        x = yield i
        print('After yield....')
        print('argument : ', x)


g = gen()
print('yield return: ', next(g))
print('yield return: ', g.send(2))
