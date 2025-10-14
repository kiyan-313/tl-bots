def dect1(func):
    def inner():
        x=func()
        return x*3
    return inner
def dect2(func):
    def inner():
        x=func()
        return x*10
    return inner

@dect2
@dect1
def test():
    return 5
print(test())