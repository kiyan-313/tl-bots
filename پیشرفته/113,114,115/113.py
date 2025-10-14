# def hello(name):
#     def hello_name():
#         print(f'Hello, {name}')
#     return hello_name
# new=hello('jamal')
# new()
#

def hello_decorator(func):

    #wrapper
    def inner():
        print('hello,this is before funtion execution')
        func()#hi user
        print('this is after funtion execution')

    return inner

@hello_decorator
def hello():
    print('hello user')

hello()
