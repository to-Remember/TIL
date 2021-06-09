a = [1,2,3]  #리스트 크기: 방의 개수. a의 크기 3
b = ['sdf', 'qwer', 'dfg']
c = [12.24, 34.45]
d = [True, True, False]

#리스트 요소: 리스트에 저장된 값 하나
#인덱스: 방번호

#print(a[3]) => 에러. 범위 밖의 인덱스. 없는 방에 접근. 현재 a는 방이 0~2까지 3개 있음
#a[3]=10  => 에러. 범위 밖의 인덱스.
a.append(4) #방을 확장하고 값 저장
print(a)
print(b)
print(c)
print(d)

#빈 리스트 생성
e = []
f = list()  #리스트 함수로 생성

e.append(1)
e.append(2)

f.append("aaa")
f.append("bbb")

print(e)
print(f)

#하나의 리스트에 다양한 타입의 값을 담을 수 있다
#파이썬은 타입에 자유로운데 이유는 모든 타입이 참조타입이기 때문
a = 10
a = 'asdf'
a = [1, 'asdf', 3.234, True]
print(a)
