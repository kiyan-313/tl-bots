def hello(fname,lname,*args,**kwargs):
    print(fname)
    print(lname)
    print(args)
    print(kwargs)

hello('amie','amiry','reza','hamid',age=23,citi='tehran',team='codyad')