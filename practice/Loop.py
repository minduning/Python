# Loop 반복문
'''
while 조건:
    실행할 명령1
    실행할 명령2

False가 되기 전까지 실행하고 돌아가고 계속 반복한다.
'''

count = 0
while count < 3:
    print('횟수:', count)
    count += 1

print('-----------------')
# continue, break
count = 0
while count < 10:
    count += 1
    if count < 4:
        continue
    print('횟수:', count)
    if count == 8:
        break
