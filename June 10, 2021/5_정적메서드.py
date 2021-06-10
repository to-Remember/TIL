#정적메서드: 클래스 안의 메서드이지만 self가 없음. 왜냐면 클래스 소속이기 대문에 객체생성 없이 클래스 이름으로 사용가능
class Test:
    x = 0

    def __init__(self):
        self.y = 0

    def method1(self):  #일반메서드 -> 클래스변수, 시점이 객체생성 이후이므로 클래스변수. 멤버변수 모두 사용 가능.
        print('method1: 멤버메서드')
        print('x:', Test.x)
        print('y:', self.y)

    def method2():  #정적메서드. 객체 생성전에 사용 가능하므로 일반 멤버 변수 사용 불가
        print('method2: 정적메서드')
        print('x:', Test.x)
        name = 'aaa'
        print()
        #print('y:', self.y)

    def method3(self):  #일반 메서드는 일반 메서드 호출도 가능. 정적메서드 호출도 가능.
        print('method3: 멤버메서드')
        self.method1()  #일반 메서드 호출
        Test.method2()  #정적 메서드 호출

    def method4():  #정적메서드. 객체 생성 전이므로 일반 메서드 호출 불가
        print('method4: 정적메서드')
        #self.method1()
        Test.method2()

def main():
    Test.method2()
    Test.method4()

    t1 = Test()
    t1.method1()
    t1.method3()

main()
