def f1():
    print('파라메터, 리턴값 없는 함수')

def f2(num):
    print('입력받은 숫자:', num)

def f3(name, age):
    print('당신의 이름은:', name)
    print('당신의 나이는:', age)


def f4(name, age):
    msg = '당신의 이름은:'+name+', 당신의 나이는:'+str(age)
    return msg

def f5(name, age):
    return name, age  #리턴값이 여러개면 하나의 튜플로 반환됨

f1()
f2(3)
f3('aaa', 12)
s = f4('aaa', 12)
print(s)
#n, a = f5('bbb', 13)
#print(n, ':', a)
t = f5('bbb', 13) #t는 튜플
print(type(t))
print('name:',t[0], ', age:',t[1])