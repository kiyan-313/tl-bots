a=['amir','ali','farid','karim','mehdi']
b=['reza','milad','amir','karim','mehdi']

c=[]

for i in a:
    for n in b:
        if i==n:
            c.append(i)
print(c)