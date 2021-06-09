#함수 정의
def hello():
    print('hello')

def add(x, y):#x, y:파라메터(매개변수)
    return x+y

def gugudan(dan):
    print('<',dan,'단>')
    for i in range(1, 10):
        print(dan,' * ', i, ' = ', dan*i)

#함수호출
hello()
res = add(1,2)#호출 시 파라메터에 넣어주는 값을 아규먼트(인자)
print(res)

for i in range(2, 10):
    gugudan(i)
