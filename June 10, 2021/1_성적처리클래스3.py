class Score: #1명의 점수 정보만 다루는 타입
    def __init__(self, kor, eng, math): #멤버 변수는 점수와 관련된 국영수총평
        self.kor = kor
        self.eng = eng
        self.math = math
        #총점 평균 계산
        self.total = self.kor + self.eng + self.math
        self.avg = self.total / 3

    def printScore(self): #점수와 관련된 국영수총평 출력
        print(self.kor, end='\t')
        print(self.eng, end='\t')
        print(self.math, end='\t')
        print(self.total, end='\t')
        print(self.avg, end='\t')
        print()

class Student: #한 학생의 정보(score포함)를 갖는 클래스
    def __init__(self, name, num, score):
        self.name = name
        self.num = num
        self.score = score #score객체. 포함관계

    def printMember(self):
        print(self.name, end='\t')
        print(self.num, end='\t')
        self.score.printScore()

def main():
    sc1 = Score(77,77,77)
    s1 = Student('A', 1, sc1)
    s1.printMember()

    s1 = Student('B', 2, Score(99,99,99)) #즉석에서 생성해도 무방하다
    s1.printMember()

main()