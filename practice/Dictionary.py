# Dictionary 관련된 정보를 서로 연관시켜놓는 것.

my_dict = {}
print(my_dict)
print(type(my_dict))

my_dict[0] = 'a'
print(my_dict)

my_dict['b'] = 2
print(my_dict)

my_dict['김민준'] = '파이썬'
print(my_dict)

print(my_dict['김민준'])
# 키를 입력하면 값이 나오게 됨.

del my_dict[0]
print(my_dict)

del my_dict['b']
print(my_dict)

# dict.values() 값만 뽑아오는 것.
print(my_dict)

for std in my_dict.values():
    print(std)

# dict.keys() 키만 뽑아오는 것.
for key in my_dict.keys():
    print(key)

# dict.items()
for key, val in my_dict.items():
    print(key, val)
