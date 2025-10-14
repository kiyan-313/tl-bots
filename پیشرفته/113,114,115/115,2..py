import time
def hello_decorator(func):

    #wrapper
    def inner(*args, **kwargs):
        begin = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(f'function execution time : ',end-begin)
    return inner

@hello_decorator
def test(name,lastname):
    time.sleep(2)
    print(f'hello {name},{lastname}')


test('jamal','sami')