'''
string.split()
함수라는 것은 어떤 기능을 수행하기 위해 모아놓은 것에 이름을 붙인 것
메소드는 함수는 함수인데 string들만 사용할 수 있는 함수이다.
'''

my_name = '김민준의 깃허브'
print(my_name.split())

fruits_str = '사과, 배, 복숭아, 수박, 망고, 딸기, 귤, 참외'
fruits = fruits_str.split()
print(fruits)
# 공백을 기준으로 다 잘린 것을 볼 수 있다.
