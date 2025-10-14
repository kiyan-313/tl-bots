# friends=['amir','reza','farid']
# m='reza' in friends
# print(m)

users={
    'amir':'1234',
    'reza':'4567',
    'farid':'6789'
}
entered_username=input('enter your username:')
entered_password=input('engter your password')
if entered_username in users:
    print('yes you are our user')
else:
    print('ohh noo you are not our user')