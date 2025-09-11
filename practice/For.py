# for

'''
for 변수 in 컨테이너
    실행할 명령1
    실행할 명령2

반복할 부분을 코드블럭, 파이썬에서는 들여쓰기가 매우 중요하다.
한번 탭을 했으면 끝까지 써야 한다.
한번 띄어쓰기 4번이면 끝까지 띄어쓰기 4번이어야 한다.
'''

animals = ['사자', '코끼리', '바다사자', '표범']

for animal in animals:
    print(animal)

for num in [1, 2, 3]:
    print(num)

for my_str in "김민준의 깃허브":
    print(my_str)
