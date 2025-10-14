child1={
    'name':'ali',
    'age':30
}
child2={
    'name':'farid',
    'age':34
}
myfamily={
    'child1':child1,
    'child2':child2
}
# myfamily={
#     'child':{
#     'name':'ali',
#     'age':30
#     },
# 'child2':{
#     'name':'farid',
#     'age':34
#     }
# }
child2=myfamily['child2']
print(child2['name'])
# print(myfamily['child2']['name'])