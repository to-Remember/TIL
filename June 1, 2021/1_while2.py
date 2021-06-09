'''
1. 1~100 합 구하라 5050
2. 1~100 짝수만 출력하라
3. 구구단 단수를 입력받아 한단 출력. 3
4. 약수 구하기(약수 구할 숫자 입력받아) 6:1,2,3,6
3*1=3
3*2=6
..
3*9=27
'''

i=1   #루프에서 사용할 변수를 정의. 카운팅 변수
while i<=100:
    print(i, end='\t')
    if i%10==0:#위에서 출력한 값이 10으로 나누어 떨어지면 엔터를 출력
        print()
    i+=1


#1~100 사이의 짝수 출력
i=1
while i<=100:
    if i%2==0:#짝수
        print(i, end='\t')
    i+=1
print()

i=2
while i<=100:
    print(i, end='\t')
    i+=2
print()

#1~100합: 1+2+3+...+100
sum=0   #누적변수
i=1     #카운팅변수
while i<=100:
    sum+=i
    i+=1
print('sum:', sum)

#구구단
dan=int(input('단수:'))
i=1 #곱하는 숫자
while i<10:
    print(dan,' * ',i,'=',(dan*i))
    i+=1

dan=2
while dan<10:
    i=1
    while i<10:
        print(dan, ' * ', i, '=', (dan * i))
        i += 1
    dan+=1

#약수. num i(1~num)까지의 숫자로 나눠서 나머지가 0인 i
num = int(input('약수구할 숫자 입력'))
i=1
while i<=num:
    if num%i==0:
        print(i, end='\t')
    i+=1
print()
#1. 1~100사이의 소수(약수가 1과 자신밖에 없는 수)를 출력

###
###
print('다운 카운팅으로 #3개 출력')
i=3
while i>0:  #down counting
    print('#',end='')
    i-=1
print()

print('업 카운팅으로 #3개 출력')
j=1
while j<3:
    i=1
    while i<4:
        print('#', end='')
        i += 1
    print()
    j+=1

#조건에 의한 반복
score = 200
while score>100 or score<0:
    score = int(input('score(0-100):'))

if score>=60:
    print('합격')
else:
    print('불합격')
