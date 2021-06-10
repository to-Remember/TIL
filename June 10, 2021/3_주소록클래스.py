'''
VO: 값 묶음
DAO: 저장소 작업. 저장, 수정, 삭제


'''


#이름, 전화, 주소
#vo (멤버를 만든 클래스를 VO(Value Object 또는 DTO(Data Transfer Object)라고 한다.
class Member:
    def __init__(self,name='',tel='',address=''):
        self.name = name
        self.tel = tel
        self.address = address
        print()

    def printMember(self):
        print('name:',self.name)
        print('tel:',self.tel)
        print('address:',self.address)

# DAO(Database Access Object) : DB에 접근하는 객체. 일단 이 코드에선 DB대신 리스트를 사용할 것. 데이터를 추가/검색/수정/삭제 기능 구현 클래스

class MemDao: #저장소 관련 작업만 담당. (리스트 작업만 전담하고 있음) -> 추가 검색 수정 삭제
    def __init__(self):
        self.datas = []

    def insert(self, m):
        self.datas.append(m)

    def select(self, name):
        for i in self.datas:
            if i.name == name:
                return i #검색된 객체의 참조값 반환. 객체에 다이렉트로 접근 가능

    def selectAll(self):
        return self.datas

    #def update(self, m): #m에다가 수정할 사람의 이름, 새전화, 새주소
    #이건 DB랑 연동할 때 필요. 이후에 학습할 것

    def delete(self, m):
        self.datas.remove(m) #이건 값을 찾아서 삭제해주는 것.
        #del self.datas[idx] -> 이건 방 번호를 알아야 함. 따라서 현재 함수에 적합하지 않음.

# Service(비즈니스 로직을 구현하는 것) : 사용자에게 제공할 기능을 구현하는 클래스. 추가/검색/수정/삭제
class MemService:
    def __init__(self):
        self.dao = MemDao()

    def addMember(self):
        name = input('name:')
        tel = input('tel:')
        address = input('address:')
        m = Member(name, tel, address)
        self.dao.insert(m)

    def printMember(self):
        name = input('search name:')
        m = self.dao.select(name)
        if m == None:
            print('없는 이름')
        else:
            m.printMember()

    def printAll(self):
        datas = self.dao.selectAll()
        for i in datas:
            i.printMember()

    def editMember(self):
        name = input('수정할 사람 name:')
        m = self.dao.select(name)
        if m == None:
            print('없는 이름')
        else:
            m.tel = input('new tel:')
            m.address = input('new address:')

    def delMember(self):
        name = input('수정할 사람 name:')
        m = self.dao.select(name)
        if m == None:
            print('없는 이름')
        else:
            self.dao.delete(m)

class Menu:
    def __init__(self):
        self.service = MemService()

    def run(self):
        while True:
            menu = int(input('1.등록 2.검색 3.수정 4.삭제 5.전체출력 6.종료'))
            if menu == 1:
                self.service.addMember()
            elif menu == 2:
                self.service.printMember()
            elif menu == 3:
                self.service.editMember()
            elif menu == 4:
                self.service.delMember()
            elif menu == 5:
                self.service.printAll()
            elif menu == 6:
                break

def main():
    m = Menu()
    m.run()

main()



'''    
    for i in range(0,3):
        name = input('name:')
        tel = input('tel:')
        address = input('address:')
        m = Member(name, tel, address)
        datas.append(m)

    for i in datas:
        i.printMember()

이렇게 하나하나 입력하기 번거로우니
위에처럼 리스트를 이용하여 루프를 돌린 것.
def main():
    m1 = Member('aaa', '111', '대한민국')
    m1.printMember()

    m2 = Member('bbb', '222', '서울')
    m2.printMember()
    
    m3 = Member('ccc', '333', '인천')
    m3.printMember()
    
'''


'''
입력을 받는 형태로.
객체를 리스트에 담을 것.
메뉴를 돌려줄 것.
'''