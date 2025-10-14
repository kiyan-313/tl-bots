users={
    'amir':'1234',
    'reza':'4567',
    'farid':'6789'
}
entered_username=input('enter your username:')
entered_password=input('engter your password')

if entered_username in users and users[entered_username]==entered_password:
    print('you loged in')
else:
    print('your password or username is wrong')


# print(users['amir'])