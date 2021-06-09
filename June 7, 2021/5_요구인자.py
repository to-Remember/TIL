#함수의 파라메터로 mutable한 값 전달의 예
#mutable: 변경되는 값. 리스트, 셋, dictionary
def f1(arr):
    print('f1안에서 변경전: ', arr)
    arr[0]=100
    print('f1안에서 변경후: ', arr)

def main():
    x = [1,2,3,4,5]
    print('main 변경전: ', x)
    f1(x)
    print('main 변경후: ', x)

main()

def f1(name, tel, age):
    print('name:', name)
    print('tel:', tel)
    print('10년 후 age:', age+10)

def main():
    n = 'aaa'
    t = '1234'
    a = 12

    f1(n, t, a)
    f1(a, n, t)

main()