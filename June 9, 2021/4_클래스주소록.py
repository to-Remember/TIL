'''
주소록
Member 클래스 정의
멤버변수
id, pwd, name, email

기능
멤버변수 출력

class Book: #Book이라는 이름의 타입을 정의

    def __init__(self, id, pwd, name, email):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.email = email

    def printBook(self):
        print('id:', self.id)
        print('pwd:', self.pwd)
        print('name:', self.name)
        print('email:', self.email)



def main():

    b1 = Book('aaa', '1111', 'a', 'a@a')
    b1.printBook()

    b2 = Book('bbb', '2222', 'b', 'b@b')
    b2.printBook()

main()
'''

class Book: #Book이라는 이름의 타입을 정의

    def __init__(self, id, pwd, name='홍길동', email='gildong@hong'):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.email = email

    def printBook(self):
        print('id:', self.id)
        print('pwd:', self.pwd)
        print('name:', self.name)
        print('email:', self.email)



def main():

    b1 = Book('aaa', '1111', 'a', 'a@a')
    b1.printBook()

    b2 = Book(id='bbb', pwd='2222', name='b', email='b@b')
    b2.printBook()

    b3 = Book('ccc', '3333')
    b3.printBook()

    b4 = b3
    b4.name = '가나다'
    b4.email = '가나다@email.com'
    b4.printBook()
    b3.printBook()


main()