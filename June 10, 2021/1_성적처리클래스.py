class Student:

    def __init__(self):
        self.name = ''
        self.num = 0
        self.kor = 0
        self.eng = 0
        self.math = 0
        self.total = 0
        self.avg = 0

    def setData(self, name, num, kor, eng, math):
        self.name = name
        self.num = num
        self.kor = kor
        self.eng = eng
        self.math = math

    def calc(self):
        self.total = self.kor + self.eng + self.math
        self.avg = self.total / 3

    def printData(self):
        print('name:', self.name)
        print('num:', self.num)
        print('kor:', self.kor)
        print('eng:', self.eng)
        print('math:', self.math)
        print('num:', self.num)
        print('total:', self.total)
        print('avg:', self.avg)

def main():
    #클래스 타입의 변수는 먼저 생성해야 사용 가능
    s1 = Student() #객체 생성
    s1.name = 'aaa'
    s1.num = 1
    s1.kor = 45
    s1.eng = 56
    s1.math = 67
    s1.calc()
    s1.printData()

main()