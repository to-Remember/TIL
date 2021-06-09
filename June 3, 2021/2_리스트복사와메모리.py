#copy 패키지 불러옴
import copy
#얕은 복사
a = [1,2,3]
b = a #참조값복사
print(a)
print(b)

a[2] = 30
print(a)
print(b)

##########
#얕은 복사2

a = [1,2,3]
b = copy. copy(a)
print(a)
print(b)

a[2] = 30
print(a)
print(b)

#########

a=[1,2,[4,5,6]]
b = copy.copy(a)
print(a)
print(b)

a[2][0] = 40
print(a)
print(b)

###############

a=[1,2,[4,5,6]]
b = copy.deepcopy(a)
print(a)
print(b)

a[2][0] = 40
print(a)
print(b)
