# 변수, 연산자, 제어문 복습!!!!!!!
'''
리스트 - 집합 데이터를 효율적으로 다루기 위해. 이후 셋 / 튜플 / 딕셔너리 배울 것
리스트 [1,2,3] -> 특징: 요소변경, 길이변경 가능
셋(집합):{1,2,3} -> 요소변경 불가.
튜플:(1,2) -> 변경 불가 -> 함수반환값
위에는 다 값만 저장, 근데 딕셔너리는 키와 값 둘다 저장.
딕셔너리: {키:값, 키:값}
'''

# 1. a는 이름의 리스트를 생성, 숫자 1,2,3,4,5로 초기화해서 생성하시오

a=[]
for i in range(1,6):
    print(i)

print()
#리스트는 만든 방 개수만큼만 사용해야 한다.

a = [1,2,3,4,5]

a=[1]*5
for i in range(0,5):
    a[i] = i+1

cnt = 1
for i in range(0,5):
    a[i] = cnt
    cnt+=1


a=[]  #방이 하나도 없다. 값 저장시 방을 만든 뒤 할당. apppend()사용
for i in range(1,6):  # i를 할당할 값
    a.append(i)  # 끝에 방을 추가하고 그 방에 값을 저장


c = [1,2,3,4,5]
a = list(c) #다른 리스트를 복사해서 생성

# 2. a의 요소를 하나씩 출력
for i in a:
    print(i, end=', ')
print()

for i in range(0, len(a)):
    print(a[i], end=',')
print()

for idx, i in enumerate(a):
    print('a[', idx, ']=', i)

# 3. a의 인덱스가 2인 요소의 값을 13으로 변경하시오
a[2]=13
print(a[2])

print()
# 4. a의 요소중 짝수만 출력
for i in a:
    if i%2 == 0:
        print(i, end=', ')
print()

# 5. a의 인덱스가 2인 요소를 삭제하시오
del a[2]
print(a)

print()

# 6. 이름이 b인 2줄 3칸 리스트를 생성. 모두 0으로 초기화해서 생성
b=[[0,0,0],[0,0,0]] # b=[[0]*3,[0]*3]
print(b[0])
print(b[1])

print()
'''
b = [0]*2
for i in range(0, len(b)):
    b[i]=[0]*3
'''

# 7. 0번줄의 2번방 요소를 10으로 변경
b[0][2] = 10
print(b[0][2])
print(b)

print()
'''
for i in range(0):
    print(b[i])
    i[2]=10

print(b)

print()
'''

# 8. b의 요소를 0번 줄은 [1,2,3], 1번 줄은 [4,5,6]으로 출력
cnt = 1
for i in range(0, len(b)):
    for j in range(0, len(b[i])):
        b[i][j] = cnt
        cnt+=1

for i in range(0, len(b)):
    for j in range(0, len(b[i])):
        b[i][j] = 3*i+j+1

b[0] = [1,2,3]
b[1] = [4,5,6]

# 9. b의 모든 요소 출력
# print(b)

for i in b: #i: [1,2,3], [4,5,6]
    for j in i:
        print(j, end=', ')
    print()
