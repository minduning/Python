#Module 모듈 -> import를 사용 '.'를 사용해서 사용할 수 있음.
# 이미 만들어져 있는 기능들 가져다 쓸 수 있음.


#random 모듈. random.choice()

import random
students = ['수박', '사과', '참외', '키위']
print(random.choice(students))
# 랜덤으로 나오게 됨.

students.append('배')
print(random.choice(students))

# random.sample()
print(random.sample(students, 2))

#로또 번호 생성기
print(random.sample(range(1, 46), 6))

#random.randint() 정수를 뽑을 수 있음.
print(random.randint(8, 10))
