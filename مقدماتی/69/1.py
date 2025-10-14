mylist=[1,3,6,7,8]

# def myfunc(number):
#     return number*2
# x=map(myfunc,mylist)

x=map(lambda a:a*2,mylist)

print(list(x))

# a=[]
# for item in mylist:
#     a.append(item*2)
# print(a)