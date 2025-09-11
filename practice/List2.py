# List

'''
100개의 숫자를 저장하려면 100개의 변수?
10000개의 숫자를 저장하려면 10000개의 변수?
LIst를 통해 해결하자.
'''

# immutable 값을 바꿀 수 없음, mutable 값을 바꿀 수 있음.
# [val1, val2, ...]


my_list = []
print(my_list)
print(type(my_list))

my_list = [1, 2, 3]
print(my_list)

std = ['김민준', '김민준1', '김민준2']
print(std)

std.append('김민준4') # List만 사용할 수 있는 함수임.
print(std)

std.append('김민준5')
print(std)

#List는 그릇이라고 생각하면 됌. 그릇을 먼저 만들고 추가를 해야 함.
