# if
'''
if 조건:
    실행할 명령1
    실행할 명령2
'''

input_name = '김민준'

if input_name == '김민준':
    print('만나서 반가워요,', input_name)

# else, elif
'''
if 조건:
    실행할 명령1
    실행할 명령2
else 조건:
    실행할 명령1
    실행할 명령2


if 조건:
    실행할 명령1
    실행할 명령2
elif 조건:
    실행할 명령1
    실행할 명령2

if 조건:
    실행할 명령1
    실행할 명령2
elif 조건:
    실행할 명령1
    실행할 명령2
else 조건:
    실행할 명령1
    실행할 명령2

elif는 많이 쓸 수 있다.
'''

name = '파이썬'

if name == '파이썬':
    print('파이썬이군요!')
elif name == '자바':
    print('자바군요!')
elif name == '자바스크립트':
    print('자바스크립트군요!')
else:
    print('너는!?')
