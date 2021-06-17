'''
클래스
int, float, str... 이러한 기본 타입으로 객체를 표현하는 것이 어려움 -> 객체 표현 가능한 데이터타입 정의.

#멤버변수는 다른 메서드에서도 만들 수 있지만 호출 순서에 따라 에러가 발생할 수 있으므로 멤버변수는 생성자에서 정의하는 것이 좋다.
class Test:
    def setData(self, a, b):
        self.a = a
        self.b = b

    def printData(self):
        print('a:', self.a)
        print('b:', self.b)
'''
#모니터 재고 관리 프로그램 > 모델명, 가격, 수량, 크기
#클래스 정의. 파이썬의 모든 클래스는 자동으로 object클래스를 상속받는다.
#그래서 object가 가지고 있는 모든 멤버변수와 메서드를 자동으로 상속받는다.
#그 중 하나가 __str__():  -> 객체를 설명하는 문자열을 반환
class Monitor:
    #생성자 -> 객체 초기화 함수. 멤버변수 정의 및 초기화 역할. self:현재 객체 참조값. 모든 메서드는 첫번재 파라메터가 self다
    #멤버변수: 객체소속의 변수, self.변수
    def __init__(self, model='', price=0, amount=0, size=0):
        self.model = model
        self.price = price
        self.amount = amount
        self.size = size

    def __str__(self):
        return 'model:' + self.model+' /price:'+str(self.price)+' /amount:' +str(self.amount)+' / size:'+str(self.size)

    def printMonitor(self):
        print('model:', self.model)
        print('price:', self.price)
        print('amount:', self.amount)
        print('size:', self.size)

def main():
    m1 = Monitor('s2440', 1500, 5, 27)
    print(m1)
    print('m1의 참조값:', id(m1))

    m2 = Monitor('BB230', 2000, 7, 25)
    print(m2)
    print('m2의 참조값:', id(m2))

    m3 = Monitor('C345e', 1700, 6, 26)
    print(m3)
    print('m3의 참조값:', id(m3))

    m4 = m3
    print(m4)
    print(id(m4))

class Service:



def main():
    monitors = [] #현재 방이 없는 상태
    monitors.append(Monitor('s2440', 1550, 5, 27))
    monitors.append(Monitor('s2447', 1555, 7, 30))
    monitors.append(Monitor('s2445', 1577, 6, 25))

    for i in range(0,3):
        print(monitors[i])

    for m in monitors:
        print(m)
        m.printMonitor()

main()