def hello_decorator(func):

    #wrapper
    def inner(*args, **kwargs):
        x=func(*args,**kwargs)
        return x.upper()
    return inner

@hello_decorator
def test(name,lastname):
    return (f'hello {name},{lastname}')

x=test('jamal','sami')

print(x)