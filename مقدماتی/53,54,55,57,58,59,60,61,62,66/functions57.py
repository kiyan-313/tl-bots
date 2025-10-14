# def hello(*names):
#     print(names)
#     print(type(names))
# hello('amir','amiri','farid')



# def hello(*names):
#     for name in names:
#         print(f'hello{name}')

# hello('amir','ali','hamid','farid','karim','rahim')



# def hello(fname,lname,*arge):
#     print(fname)
#     print(lname)
#     print(arge)

# hello('amir','ali','hamid','farid','karim','rahim')



def a(*kids):
    print('the youngest child is '+kids[2])

a('emil','tobias','linus')
