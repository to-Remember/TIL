class Member:
    def __init__(self, id='', pwd='', email=''):
        self.__id = id
        self.__pwd = pwd
        self.__email = email

    def setId(self, id):#private 멤버 값을 설정하는 메서드
        self.__id = id

    def getId(self):#private 멤버 값을 리턴해주는 메서드
        return self.__id

    def __str__(self):#object 클래스로부터 상속받은 메서드 재정의. 이메서드 역할은 객체 설명. '클래스명, 참조값'
        return 'id:'+self.__id+' / pwd:'+self.__pwd+' / email:'+self.__email

def main():
    m1 = Member('aaa', '111', 'aaa@email.com')
    m2 = Member('bbb', '222', 'bbb@email.com')
    m3 = Member('ccc', '333', 'ccc@email.com')
    #m1.__id
    m1.setId('aaa1')
    print('m1.a:', m1.getId())

    print(m1)
    print(m2)
    print(m3)

main()