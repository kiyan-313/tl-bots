def myfunc(name):
    ups=0
    lows=0
    for a in name:
        if a.isupper():
            ups+=1
        elif a.islower():
            lows+=1
        else:
            pass

    print(f'upper cases: {ups}')
    print(f'lower cases: {lows}')
while True:
    name=input('enter your name:')
    myfunc(name)