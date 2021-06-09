#emails = []
#이메일을 등록하고 검색하는 함수(몇번방에 있다)


emails=[]

def addEmail():#등록하는 함수. 중복허용 안됨. 이메일 입력받아 리스트 추가
    while True:
        email = input('등록할 이메일:')
        #이메일 중복체크
        res = searchEmail(email)
        if res == None:
            break
        else:
            print('중복된 이메일임. 다시 입력하시오')

    emails.append(email)


def searchEmail(s_email):#파라메터로 검색할 이메일을 받아서 emails리스트에서 검색하여 있으면 인덱스, 없으면 아무값도 반환안함
    for idx, i in enumerate(emails):
        if i==s_email:
            return idx
    #동일한 이메일이 있으면 idx(인덱스)를 반환하고 없으면 None이 반환됨

def printEmail():#검색된 이메일 출력
    email = input('검색할 이메일을 입력:')
    idx = searchEmail(email)
    if idx == None:
        print('없는 이메일')
    else:
        print(idx, '번째 방에 있음 / ', emails[idx])

def printAll():
    print('등록된 이메일')
    for i in emails:
        print(i)

def main():
    while True:
        menu = input('1.등록 2.검색 3.전체출력 4.종료')
        if menu=='1':
            addEmail()
        elif menu=='2':
            printEmail()
        elif menu=='3':
            printAll()
        elif menu=='4':
            break

main()