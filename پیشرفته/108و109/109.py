names=['amir','milad','hossin','reza','mehdi']
# newlist=[name for name in names if 'a' in name]
# print(newlist)

# numbers=[1,2,3,4,5,6,7,8,9]
# nwelist=[number *2 for number in numbers ]
# print(nwelist)

# newlist=[name.upper() for name in names]
# print(newlist)

# newlist=[x for x in range(15) if x < 6]
# print(newlist)

# newlist=['hello' for x in range(10) if x <6]
# print(newlist)

newlist=[name if name !='amir' else 'jafar' for name in names]
print(newlist)