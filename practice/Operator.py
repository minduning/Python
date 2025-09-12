# Comparison 비교 연산자
# == != > < <= >=

print(1 < 2)
print(1 != 1)
print(5 <= 5)

# Logical 논리 연산자
# and or not
print(True)
print(False)

print(True and True)
print(True and False)
print(False or True)
print(True or False)
print(False or False)

print(not True)
print(not False)

height = 120
age = 8

print(height > 140 and age > 10)

# Membership 멤버쉽 연산자
김민준의_깃허브 = ['가', '나', '다', '라', '마', '바']
print(김민준의_깃허브)

print('나' in 김민준의_깃허브)
print('사' in 김민준의_깃허브)
print('사' not in 김민준의_깃허브)

김민준의_깃허브.append('사')
print(김민준의_깃허브)
print('사' in 김민준의_깃허브)
