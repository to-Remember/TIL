'''
피카추
--변수(상태값)
hp(에너지상태) 0이면 죽음. 30
exp(경험치) 0
lv(경험치 20마다 레벨1증가) 1

기능=>함수로구현
밥먹기: #hp 5증가
잠자기: hp 10증가
운동하기: hp 15감소. exp 15증가
놀기:hp 5감소. exp 7증가. hp감소(죽었나?). exp증가(레벨업체크)
종료
'''
#초기값
hp = 30
exp = 0
lv = 1


def eat(hp):
    print('밥을 먹었습니다')
    hp += 5
    return hp

def sleep(hp):
    print('잠을 잤습니다')
    hp += 10
    return hp

def play(hp,exp,lv):
    print('놀았습니다')
    hp -= 5
    if hp <= 0:
        print('사망했습니다')
        exit()
    exp += 7
    if exp >= 20:
        lv += 1
        exp -= 20
        print('레벨업 했습니다')
    return hp, exp, lv


def exercise(hp,exp,lv):
    print('운동을 했습니다')
    hp -= 15
    if hp <= 0:
        print('사망했습니다')
        exit()
    exp += 15
    if exp >= 20:
        lv += 1
        exp -= 20
        print('레벨업!!')
    return hp, exp, lv

while True:
    m = int(input('1. 밥을먹는다 2. 잠을잔다 3. 신나게논다 4. 운동을한다 5. 게임종료: ' ))
    if m == 1:
        hp = eat(hp)
    elif m == 2:
        hp = sleep(hp)
    elif m == 3:
        hp,exp,lv = play(hp,exp,lv)
    elif m == 4:
        hp,exp,lv = exercise(hp,exp,lv)
    elif m == 5:
        print('게임종료')
        exit()

    print('stat: ')
    print('hp:',hp,'exp:', exp, 'lv:', lv)

'''while True:
    menu = int(input('1.밥먹기 2.잠자기 3.놀기 4.운동하기 5.종료'))
    if menu==1:
        print('밥먹는다')  #hp 5증가
        hp+=5
    elif menu==2:
        print('잠잔다')    #hp 10증가
        hp+=10
    elif menu==3:
        print('논다')     #hp 5감소. exp 7증가. hp감소(죽었나?). exp증가(레벨업체크)
        hp-=5
        if hp<=0:
            print('캐릭터 사망')
            break
        exp+=7
        if exp>=20:
            lv+=1
            exp-=20
            print('레벨 1상승')
    elif menu==4:
        print('운동한다')   #hp 15감소. exp 15증가
        hp -= 15
        if hp <= 0:
            print('캐릭터 사망')
            break #게임종료
        exp += 15
        if exp >= 20:
            lv += 1
            exp -= 20
            print('레벨 1상승')
    elif menu==5:
        print('종료')
        break  #루프 빠져나감
    print('상태확인')
    print('hp:',hp, ' / exp:',exp, ' / lv:', lv)

print('게임종료')'''