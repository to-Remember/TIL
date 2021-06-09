def f1(name, tel, age=5):#age=5: 아규먼트 기본값
    print('name:', name)
    print('tel:', tel)
    print('10년 후 age:', age+10)

def main():
    n = 'aaa'
    t = '1234'
    a = 12

    #키워드 인자
    f1(tel=t, age=a, name=n)
    f1(n, t)
main()