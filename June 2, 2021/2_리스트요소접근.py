a=[1,2,3]
print(a[0])#리스트의 0번방 값 출력
print(a[1])
print(a[2])

for i in range(0, 3):#i:인덱스. 방번호
    print(a[i], end=', ')
print()
for i in a:#i:요소
    print(i, end=', ')
print()

b = ['aaa', 'bbb', 'ccc']
print('b의 길이: ', len(b))
print('asdfas의 길이: ', len('asdfas'))
print('b의 요소 출력')
for i in range(0, len(b)):
    print(b[i], end=', ')
print()

for i in b:#i:요소
    print(i, end=', ')
print()

#숫자 10개를 입력받아서 리스트에 저장한 뒤 출력하라
data=[0]*10 #리스트를 0으로 초기화한 방 10칸 생성
print(data)
for i in range(0, len(data)):
    data[i] = int(input('num:'))

for i in data:
    print(i, end=', ')
print()

data2 = []#방이 0개
for i in range(10, 20):
    x = int(input('num:'))
    data2.append(x)
print(data2)

#5명 학생의 점수를 입력받아 총점과 평균을 출력하라
score = [0]*5
sum1 = 0
for i in range(0, 5):
    score[i] = int(input('score:'))
    sum1 += score[i]#총점에 누적

avg1 = sum1/len(score)
print('sum:', sum1, ' / avg:', avg1)

s = sum(score)

print('sum:', s)
