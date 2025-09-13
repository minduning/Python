# Function
'''
def 함수이름(인자1, ...)
    실행할 명령1
    실행할 명령2

    return 결과
'''

def add(num1, num2):
    return num1 + num2

print(add(1, 2))


def add_mul(num1, num2):
    return num1 + num2, num1 * num2

print(add_mul(1, 2))
# 소괄호로 나옴. 튜플로 던짐. 함수는 1개의 튜플을 던져준다.
