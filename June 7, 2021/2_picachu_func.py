hp = 30
exp = 0
lv = 1

def 밥먹기():
    global hp  #hp는 전역변수임을 의미
    print('피카추 밥먹음')
    hp += 5

def 잠자기():
    global hp  #전역변수라고 지정하는 것
    print('피카추 잠잠')
    hp += 10

def 놀기():
    global hp, exp  #전역변수라고 지정하는 것
    print('피카추 논다')
    hp -= 8
    flag = hp > 0 #살아있다면 아래와 같이 경험치 추가
    if flag:
        exp += 5
        레벨체크()
    return flag

def 운동하기():
    global hp, exp  #전역변수라고 지정하는 것
    print('피카추 운동한다')
    hp -= 15
    flag = hp > 0
    if flag:
        exp += 10
        레벨체크()
    return flag

def 상태확인():
    print('피카추 상태확인')
    print('hp:',hp)
    print('exp:',exp)
    print('lv:',lv)

def 레벨체크():
    global hp, exp, lv
    if exp >= 20:
        lv += 1
        exp -= 20
        print('레벨 1 상승')

def main():
    flag = True
    while flag:
        menu = input('1.밥먹기 2.잠자기 3.운동하기 4.놀기 5.상태확인 6.종료')
        if menu == '1':
            밥먹기()  # 앞에 hp랑 뒤에 파라메터 있어야지 변경된 값이 리턴됨
        elif menu == '2':
            잠자기()
        elif menu == '3':
            flag = 운동하기()
        elif menu == '4':
            flag = 놀기()
        elif menu == '5':
            상태확인()
        elif menu == '6':
            print('게임종료')
            break
        if not flag:
            print('캐릭터 사망')


main()
