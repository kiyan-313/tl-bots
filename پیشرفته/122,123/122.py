# def gertot():
#     yield 1
#     yield 2
#     yield 3
# for x in gertot():
#     print(x)

# def gertot():
#     yield 1
#     yield 2
#     yield 3
# x=gertot()
# for i in x:
#     print(i)


def fib(limit):
    # a, b = 0, 1
    a=0
    b=1
    fibs=[]
    while len(fibs) < limit:
        # fibs.append(a)
        yield a
        # a, b = a, b + a
        a=b
        b=a+b
    # print(len(fibs))
    # return fibs
x = fib(100)

for value in x:
    print(value)
