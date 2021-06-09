def 더하기(a, b):#a, b:계산할 숫자 2개
    c=a+b
    return c

def 빼기(a, b):
    return a-b

def 곱하기(a, b):
    return a*b

def 나누기(a, b):#함수에서 아무값도 반환하지 않으면 None객체 전달됨
    if b!=0:
        return a/b

'''
x = 6
y = 3
print(x,' + ', y, ' = ', 더하기(x, y))
print(x,' - ', y, ' = ', 빼기(x, y))
print(x,' * ', y, ' = ', 곱하기(x, y))
res = 나누기(x, y)
if res==None:
    print('0으로 나눌 수 없음')
else:
    print(x,' / ', y, ' = ', res)
'''

num1 = int(input('num1:'))#계산할 숫자1
num2 = int(input('num2:'))#계산할 숫자2
res = None  #계산 결과 담을 변수. None:값이 없다는 의미의 상수
op = input('op(+, -, *, /):')#연산자
if op=='+':
    res = 더하기(num1, num2)
elif op=='-':
    res = 빼기(num1, num2)
elif op=='*':
    res = 곱하기(num1, num2)
elif op=='/':
    res = 나누기(num1, num2)

if res == None:
    print('잘못된 수식')
else:
    print(num1, op, num2, '=', res)
