def hello_decorator(func):

    #wrapper
    def inner(*args, **kwargs):
        print('hello,this is before funtion execution')
        func(*args,**kwargs)#hi user
        print('this is after funtion execution')

    return inner

@hello_decorator
def hello(name,lastname):
    print(f'hello {name},{lastname}')

hello('jamal','sami')
