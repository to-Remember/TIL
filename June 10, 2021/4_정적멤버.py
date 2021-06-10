#파이썬 클래스 특징
#정적멤버변수 정적메서드
class Test:
    x = 0  #클래스 변수. 정적 멤버 변수. 정적메모리(static)에 저장. 이 클래스로 만든 모든 객체는 공용으로 사용한다.
    def __init__(self):
        self.y = 0 #일반멤버변수 (앞에 self를 꼭 붙인다. 이 멤버변수는 self객체 소속)

    def printxy(self):
        print('x:',Test.x)
        print('y:',self.y)

def main():
    print(Test.x) #객체 생성 전에도 사용 가능. 메모리 특징때문에.
    #print(t1.y) #일반멤버변수는 객체 사용 전에 사용 불가

    t1 = Test()
    Test.x+=1
    t1.y += 1
    t1.printxy()

    t2 = Test()
    Test.x += 1
    t2.y += 1
    t2.printxy()

    t3 = Test()
    Test.x += 1
    t3.y += 1
    t3.printxy()
