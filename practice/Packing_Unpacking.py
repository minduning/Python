# Packing_Unpacking

my_tuple = 1, 2, 3
num1, num2, num3 = my_tuple

print(num1)
print(num2)

num1, num2 = num2, num1
print(num1)
print(num2) # 값이 분배가 되었음.
