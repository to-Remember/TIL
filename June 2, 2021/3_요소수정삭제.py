#리스트도 요소를 변경할 수 있다 => 요소 수정/삭제 가능
a = [1,2,3,4,5]
print(a)

a[2]=30#수정. 값 재할당
print(a)

del a[2]  #2번방 삭제
print(a)

del a[1:3] #범위로 삭제(1~2)
print(a)

a.remove(1)#값을 찾아서 삭제.
#a.remove(10)# 없는 값이면 에러
print(a)

b = [2,7,4,5,3]
print(b.index(7))
#print(b.index(70)) =>없는 값 에러
list.sort(b)#정렬
print(b)