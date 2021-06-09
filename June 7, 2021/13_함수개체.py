'''
함수 객체
함수를 변수에 담음

def f1(name):
    print(name, ' hello')

def main():
    #obj => 함수 객체
    obj = f1  #함수이름에는 함수 참조값이 있다
    obj('aaa')

main()

1. 핸들러로 활용: 함수를 다이렉트로 호출하지 않고 이벤트 핸들러로 등록해서 사용하고자 할때 사용할 수 있다
def onEvent(f):
    print('이벤트 등록')
    f()#함수 객체로 함수 대신 호출

def handler():
    print('3의 배수')

def main():
    for i in range(1, 100):
        print(i)
        if i%3==0:
            onEvent(handler)
main()
2. 룩업테이블(리스트): 함수를 리스트에 담고 제어문 대신 인덱스를 활용해서 함수를 호출하면 성능향상을 볼 수 있음

'''

def 밥먹기():
    print('피카추 밥먹음')

def 잠자기():
    print('피카추 잠자기')

def 놀기():
    print('피카추 놀기')

def 운동하기():
    print('피카추 운동하기')

def main():
    funcs = [밥먹기, 잠자기, 놀기, 운동하기]
    menu = int(input('1.밥먹기 2.잠자기 3.놀기 4운동하기'))
    funcs[menu-1]()

main()
