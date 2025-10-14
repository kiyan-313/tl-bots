usernanme=input('enter your username: ')

def validation(username):
    if len(username)>8:
        return False
    else:
        return True
    
    print('hello')

if validation(usernanme):
    print('your username is ok:')
else:
    print('ypur username is wrong')