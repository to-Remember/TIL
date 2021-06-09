import sys

a=10
b=13
#조건문은 조건이 만족될때만 실행됨

if a>b:#거짓. False
    print('a는 b보다 크다')

print('이건 if랑 상관없음')

if a==b:
    print('a는 b와 같다')

if a<b:#조건이 True이므로 블록이 실행됨
    print('a는 b보다 작다')

#합격 불합격 체크
score = int(input('점수:'))
if score>=60:
    print('합격')
else:#if 조건이 만족되지 않으면 실행되는 블록. score<60
    print('불합격')

#짝수, 홀수 체크
num = int(input('num:'))
if num%2==0:
    print('짝수')
else:
    print('홀수')

#성인 여성 인증
age = int(input('나이:'))

if age>=20:  #age가 20이상
    gender = input('성별(여:f, 남:m):')
    if gender=='f':
        print('입장')
    else:
        print('여성만 입장가능')
else:
    print('성인만 입장가능')


#성인 여성 인증 - 2
age = int(input('나이:'))
gender = input('성별(여:f, 남:m):')

if age>=20 and gender=='f':
    print('입장')
else:
    print('성인 여성만 가능')

#
age = int(input('나이:'))
gender = input('성별(여:f, 남:m):')

if age>=20 or gender=='f':
    print('입장')
else:
    print('성인이거나 여성이면 가능')

menu=2
if menu==1:
   print('game start')
elif menu==2:
   print('select char')
elif menu==3:
   print('exercise')
elif menu==4:
   print('game over')
else:
   print('잘못 입력했다')
'''
점수를(0-100) 입력받아서 학점 출력
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 60미만
'''

score = int(input('score(0-100):'))
if score<0 or score>100:
    print('잘못된 점수')
else:
    if score >= 90: #90<=score<=100:
        print('A')
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")