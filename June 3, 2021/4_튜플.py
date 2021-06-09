'''
튜플(tuple)
요소 변경X (우회적으로 변경 가능 - mutable), 튜플도 변경X
고정된 집합 데이터 저장, 읽는 작업
여러개의 값을 한번에 초기화하는 작업에 많이 사용

a, b, c = 1, 2, 3 #묵시적 튶플 사용
print(a)
print(b)
print(c)
'''

#튜플 생성
t1 = (1,2,3)
for i in t1:
    print(i, end=', ')
print()

for i in range(0, len(t1)):
    print(t1[i], end=', ')
print()

t2 = ('asd', 12, True, [3,4,5])
print(t2)

#빈 튜플 생성
t3 = ()
print(type(t3))

t4 = (1) # 만약 괄호 안에 숫자가 있다면 int로 되기에 숫자를 넣고 싶다면 뒤에 콤마를 같이 넣어야 함
print(type(t4))

t5 = (1,)
print(type(t5))

#다차원 튜플
s1 = ((1,2,3),[4,5])
for i in range(0, 2):
    for j in range(0, len(s1[i])):
        print('s1[',i,'][',j,'j=',s1[i][j])

for i in s1:
    print(type(i))
    for j in i:
        print(j, end = ', ')
    print()

#요소 수정, 삭제 불가
t1 = (1,2,3,4,[5,6,7])
# t1[0] = 10 -> 생성 이후 =연산자 사용 불가
t1[4][0] = 50
print(t1)

del t1[4][0]
print(t1)


