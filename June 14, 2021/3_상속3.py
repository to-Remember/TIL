#학생, 교수, 교직원 클래스에 상속해줄 부모 클래스
class Person:
    def __init__(self):
        self.number = 0 #번호
        self.name = ''  #이름
        self.type = ''  #타입(교직원, 교수, 학생)
        self.dept = ''  #학과나 부서

    def printInfo(self):
        print('number:', self.number)
        print('name:', self.name)
        print('type:', self.type)
        print('dept:', self.dept)

class Student(Person):
    def __init__(self, number, name, dept):
        super().__init__()
        self.number = number
        self.name = name
        self.dept = dept
        self.type = '학생'
        self.subj = []#수강과목목록

    def 수강신청(self, sub):
        self.subj.append(sub)

    def print수강과목(self):
        print('수강과목')
        for i in self.subj:
            print(i)

class Prof(Person):
    def __init__(self, number, name, dept):
        super().__init__()
        self.number = number
        self.name = name
        self.dept = dept
        self.type = '교수'
        self.담당과목 = []  #담당할 과목목록

    def 담당과목추가(self, sub):
        self.담당과목.append(sub)

    def print담당과목(self):
        print('담당과목')
        for i in self.담당과목:
            print(i)

class Staff(Person):
    def __init__(self, number, name, dept):
        super().__init__()
        self.number = number
        self.name = name
        self.dept = dept
        self.type = '교직원'
        self.job = ''   #직무

    def setJob(self, job):
        self.job = job

    def printJob(self):
        print('담당직무:', self.job)

def main():
    s1 = Student(1, 'aaa', '컴퓨터공학')
    s1.수강신청('전산학개론')
    s1.수강신청('컴퓨터비전')
    s1.printInfo()
    s1.print수강과목()

    p1 = Prof(2, 'bbb', '전자공학')
    p1.담당과목추가('c언어')
    p1.담당과목추가('VHDL')
    p1.printInfo()
    p1.print담당과목()

    s2 = Staff(3, 'ccc', 'HR')
    s2.setJob('인재양성')
    s2.printInfo()
    s2.printJob()

main()


