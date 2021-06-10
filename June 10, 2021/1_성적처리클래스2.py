class Student:
    def __init__(self, name='', num=0, score=[]):
        self.name = name
        self.num = num
        self.score = score #국영수 총점 및 평균 담을 리스트

    def calc(self):
        for i in range(0,3):
            self.score[3] += self.score[i]

        self.score[4] = self.score[3] / 3

    def printInfo(self):
        print(self.name, end = '\t')
        print(self.num, end = '\t')
        for i in self.score:
            print(i, end = '\t')
        print()

def main():
    s1 = Student('AA', 1, [55,55,55,0,0]) #객체 생성, 메모리 할당, 메모리 초기화
    s1.calc()
    s1.printInfo()

    s2 = Student('BB', 2, [77,77,77,0,0])
    

main()

