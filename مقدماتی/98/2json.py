import json
x={
    'name':"john",
    'age':30,
    'city':'new york',
    'isteacher':True,
    'lastname':None
}
y=json.dumps(x)
print(y)
print(type(y))