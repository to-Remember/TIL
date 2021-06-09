'''
셋(set): 집합
요소 중복 허용 안됨
순서 없음
요소 변경 불가. immutable 이어야 함.
셋 자체는 변경 가능(요소 추가/삭제 가능)
'''

#셋 생성
a = [1,2,0,4,3,2,4]
a[0]
a[1]

s = {1,2,3}
print(s)
print(type(s))

s = {} #주의!!칸이 비어있으면 딕셔너리가 됨!!
print(type(s))

#set은 요소 순서 없기 때문에 인덱스가 없음
s = {1,2,3} #중복된 값이 있으면 에러 없이 저장 안함
for i in s:
    print(i)

s = {'aaa',1,True}  #이렇게 다양한 타입 넣을 수 있음
print(s)

#s={1,2,{3,4,5]}
#print(s)
#불가!! 셋은 변경가능한 요소를 가질 수 없기에

#셋에 요소 추가하려면 add함수 이용
s.add('bbb') #요소 한개 추가
print(s)

a = [5,6,7]
s.update(a) #요소 여러개 추가
print(s)

#요소 삭제
s.remove('aaa') #없는 요소 삭제시 에러
s.discard(1) #없는 요소 삭제시 무시
print(s)

x = s.pop() #하나씩 삭제
print(x, '가 삭제됨')
print(s)

x = s.pop()
print(x, '가 삭제됨')
print(s)

s.clear() #모든 요소 삭제. 리스트에서도 동일
print(s)

##########
#합집합
s1 = {1,2,3}
s2 = {3,4,5}

s3 = s1|s2
print(s3)

s4=sl.union(s2)
print(s4)

#교집합
s3 = s1 & s2
print(s3)

s4 = s1.intersection(s2)
print(s4)

#차집합
s3 = s1 - s2
print(s3)

s4 = s2 - s1
print(s4)

s5 = s1.difference(s2)
print(s5)



