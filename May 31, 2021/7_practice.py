a = 5
while a > 0:
    print(a)
    a -= 1

print('while밖')

a = 1
while a < 11:
    print(a)
    a += 1

# 1. 1-100 합 구하라 5050

a = 1
while a < 5050:
    print(a)
    a += 1

i = 1  # 루프에서 사용할 변수를 정의. 카운팅 변수
while 1 <= 100:
    print(i, end='\t')
    if 1 % 10 == 0:  # 위에서 출력한 값이 10으로 나누어 떨어지면 엔터를 출력
        print(i)
    i += 1


# 2. 1-100 짝수만 출력하라
i = 1
while i <= 100:
    if i % 2 == 0:  # 짝수
        print(i, end='\t')
        i += 1
print()

i = 2
while i <= 100:
    print(i, end='\t')
    i += 1
print()

# 3. 구구단 단수를 입력받아 한단 출력 (3*1=3)
# (1)
a = 2
while (a < 10):
    b = 1
    while (b < 10):
        print("{} * {} = {}".format(a, b, a * b))
        b += 1
    a += 1
print('2단')
# (2)
for i in range(1, 10):  # 1부터 9까지
    print(f'2 x {i} = {2 * i}')
for dan in range(2, 10):
    print(f'{dan}단')  # 몇단인지 표시
    for i in range(1, 10):
        print(f'{dan} x {i} = {dan * i}')
    print('-' * 10)  # 한개의 단이 끝나면 구분선

dan = int(input('단수:'))
i = 1
while i < 10:
    print('dan', '*', i, '=', (dan * i))
    i += 1

dan = 2
while i < 10:
    i = 1
    while 1 < 10
        print(dan, '*', i, '=', (dan * i))
        i += 1
    dan += 1

# 4. 약수, num i(1~num)까지의 숫자로 나눠서 나머지가 0인 i
num = int(input('약수 구할 숫자 입력'))
i=1
while i<=num:
    if num%1==0:
        print(i, end='\t')
    i+=1

