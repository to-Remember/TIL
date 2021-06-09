'''
index 함수 사용하지 말고 탐색
리스트에 10개 숫자 입력받아서 저장
1. 최대값, 최소값 출력
max=첫요소 #가장큰값 담을 변수
max의 값과 각 방의 값을 비교해서 현재 max 값보다 큰 값이면 바로 max할당

2. 찾고싶은 값 입력받아서 그 값의 위치 출력. 없으면 없다고 출력
 s_num=input()
 for 배열길이만큼
     if s_num==a[i]:
         있다
     else:
         없다
---------enumerate()연습----
a=[2,8,6,4]
for idx, i in enumerate(a):
    print(idx, ':', i)
-------------------------
'''

#숫자 10개 입력받아 저장
#a = [0]*10 =>[0,0,0,0,0,0,0,0,0,0]. 인덱스로 값 저장 가능(0~9)
a = []  #빈 리스트 생성.
for i in range(0, 10):#10회 반복.
    a.append(int(input('num:')))

print(a)

#요소 중 최대값 찾기
max = a[0]  #min:최대값을 담을 변수
for i in a:
    if max<i:   #i가 최대값
        max = i
print('max:', max)

#요소 중 최소값 찾기
min = a[0]  #min:최소값을 담을 변수
for i in a:
    if min > i: #i가 최소값
        min = i
print('min:', min)

s_num = int(input("검색할 숫자:"))
flag = True #찾았는지 표시. 못찾았을때 True, 찾았을때 False.
for i in range(0, len(a)):
    if a[i]==s_num:
        print(i, '번째 방에 있음')
        flag = False
        break
if flag:#flag가 True이면 if문은 True가 되므로 실행
    print('not found')

'''
찾았으면 flag는 False가 되고
못찾았으면 flag는 True
'''
'''
max = a[0] #첫 요소 할당(초기 기준값). 현재까지 가장 큰 값 저장
max_idx = -1
for idx, i in enumerate(a):  #
    if max < i:#max보다 더 큰 값을 만나면 max를 그 값으로 교체
        max=i
        max_idx=idx
print('max:', max, ' / max위치:', max_idx)


min = a[0]
min_idx = -1
for idx, i in enumerate(a):  #
    if min > i:
        min=i
        min_idx=idx
print('min:', min, ' / min위치:', min_idx)



#순차 탐색
s_num = int(input("검색할 숫자:"))
flag = True#찾았나 표시. 못찾았을때 True,
for idx, i in enumerate(a):
    if s_num == i:
        print(idx,' 방에 있음')
        flag = False
        break
if flag:
    print('not found')
'''

