# x=10
# def test():
#     global x
#     x+=7
# test()
# print(x)

def test():
    x=9

    def test2():
        # global x
        nonlocal x
        x=18
        print(x)

    test2()
    print(x)
test()
# print(x)