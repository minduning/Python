# Arithmetic 산술 연산자
# + - * /

print(3 + 3)
print(6 * 2)
print(12 / 3)

# 특수 연산자 ** // %
# ** 제곱
# // 몫
# % 나머지

print(3 ** 2)
print(4 ** 3)

print(7 / 3)
print(7 // 3)
print(7 % 3)


numbers = [1, 2, 3, 4, 5, 6, 7]

for number in numbers:
    print(number)

if 1 % 2 == 1:
    print("홀수")

if 2 % 2 == 0:
    print("짝수")


print(numbers)

for number in numbers:
    if number % 2== 1:
        print(number, "는 홀수!")
    else:
        print(number, "는 짝수")
