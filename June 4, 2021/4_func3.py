#파라메터로 숫자를 받아서 그 숫자의 약수 출력하는 함수. 리턴값 없음
def 약수(num):
    print(num, '의 약수: ', end='')
    for i in range(1, num+1):
        if num%i == 0:
            print(i, end=', ')
    print()

#x = int(input('num:'))
#약수(x)

def 약수2(num):
    res = []
    for i in range(1, num+1):
        if num%i == 0:
            res.append(i)
    return res

def 약수프린트(data):
    print(data[len(data)-1], '의 약수: ', end='')
    for i in data:
        print(i, end=', ')
    print()

x = int(input('num:'))
d = 약수2(x)
약수프린트(d)