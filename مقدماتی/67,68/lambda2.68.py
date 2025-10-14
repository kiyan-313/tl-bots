def myfunc(n):
    # def new(a):
    #     return a*n
    # return new
    return lambda a:a*2
mydoubler=myfunc(2)

print(mydoubler(5))