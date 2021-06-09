class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def printPoint(self):
        print('좌표:(',self.x,' , ', self.y,')')

class Test:
    def __init__(self):
        self.p = Point()   #None 상수
        self.num = 0    #int 값

def main():
    t1 = Test() #Test 객체 생성 => 메모리 할당. 생성자를 호출해야 객체 메모리를 할당받는다
    t1.num = 10
    t1.p.x = 10
    t1.p.y = 20
    t1.p.printPoint()

main()