b=[1,2,3,4,5]

print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])

for i in [1,2,3,4,5]:
    print(i)

for i in b:
    print(i)

for i in 'hello world':
    print(i)

for i in range(0,5):#[0,1,2,3,4]
    print(i)

for i in range(1,10,2):#[1,3,5,7,9]. range(시작값, 끝값, 간격)
    print(i)
'''
1. 1~10출력
2. 1~10사이의 짝수 출력
3. 1~100까지 합
4. 구구단 3단
'''
#1~10출력
for i in range(1, 11):
    print(i, end=', ')
print()

#1~10사이의 짝수 출력
for i in range(2, 11, 2):
    print(i, end=', ')
print()

#1~10사이의 짝수 출력
for i in range(1, 11):
    if i%2==0:
        print(i, end=', ')
print()

#1~100까지 합
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

dan=3
#곱하는 숫자:1~9
for i in range(1, 10):
    print(dan,' * ', i,' = ', (dan*i))

###
###
for j in range(0, 2):
    for i in range(0, 3):#0,1,2
        print('#', end='')
    print()

for dan in range(2, 10):
    for i in range(1, 10):
        print(dan, ' * ', i, ' = ', (dan * i))


for i in range(1, 11):#1~10
    if i%2==0:#짝수이면
        continue

    print(i, end='\t')
print()
