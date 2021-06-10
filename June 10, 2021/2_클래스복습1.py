'''
Person 사람, 이름, 나이 저장, 기능 출력
객체 2개 생성
클래스: 멤버변수(속성)과 메서드 두 개로 구성된다.
'''


'''
(1) 기본기 다지기 (코드 지저분)
class Person:
    def __init__(self): #생성자
        #멤버 변수 정의. 객체의 데이터를 담는 변수.
        self.name = ''
        self.age = 0

        #리스트라면 self.arr = [] 이렇게 초기화
        #객체타입(객체형)이면 self.point = None
        #물론 클래스는 타입을 안가려서 아무렇게 입력해도 되지만 위 형식을 지키는 것이 바람직

    #메서드. 클래스 안에 정의한 함수. 이 객체의 기능. 정보 출력
    #멤버변수는 항상 self를 붙이며, 이는 현재객체를 뜻한다(물론 self말고 다른 문자 입력 가능.이름은 기능이 없기에).
    #모든 메서드의 첫번째 파라미터는 현재 객체의 참조값이 자동으로 전달된다.
    def printPerson(self):
        #name = 'xxx' -> 이건 지역변수
        print('name:', self.name)
        print('age:', self.age)


def main():
    p1 = Person() #생성자 호출은 -> 클래스명() -> 객체가 사용할 메모리 할당받아 참조값을 반환함.
    #반환받은 참조값을 변수 p1에 저장
    p1.name = 'Apple' #멤버 변수값 쓰기
    p1.age = '20' #멤버 변수값 쓰기
    
    #print(p1.name) #멤버 변수값 읽기
    #print(p1.age) #멤버 변수값 읽기
    #필요없는 코드. 출력하는 메소드를 이미 만들어놨기에
    
    p1.printPerson()

    p2 = Person()
    p2.name = 'Banana'
    p2.age = '7'
    
    #print(p2.name) #멤버 변수값 읽기
    #print(p2.age) #멤버 변수값 읽기

    p2.printPerson()


밑의 내용 추가 가능:
    persons = [] #밑의 리스트를 담을 객체를 생성한 것
    for i in range(0,3) #객체 3개 만들어서 루프 돌리기


main()'''


class Person:
    def __init__(self, name='', age=0):  # 생성자
        # 멤버 변수 정의. 객체의 데이터를 담는 변수.
        self.name = name
        self.age = age

    def setData(self, name, age):
        self.name = name
        self.age = age

    def printPerson(self):
        name = 'xxx' #지역변수
        print('지역변수 name:', name)
        print('name:', self.name)
        print('age:', self.age)


def main():
    p1 = Person('aaa',12)  # 생성자 호출은 -> 클래스명() -> 객체가 사용할 메모리 할당받아 참조값을 반환함.
    p1.printPerson()

    p2 = Person()
    p2.printPerson()



main()

