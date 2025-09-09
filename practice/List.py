my_list = [1, 2, 3]

students = ['a', 'b', 'c', 'd']
students.append('e')

print(students)

# 튜플은 그 값을 바꿀 수 없다
students[0] = 'x'
print(students)

my_tuple = (1, 2, 3)
print(my_tuple)
# my_tuple[0] = '4' 이렇게 바꾸려고 해도 값을 바꿀 수 없음

my_dict = {'김': '남자', '민': '여자', '준': '남자'}
print(my_dict['김'])
