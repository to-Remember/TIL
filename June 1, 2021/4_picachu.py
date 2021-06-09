'''
피카추
--변수(상태값)
hp(에너지상태) 0이면 죽음. 30
exp(경험치) 0
lv(경험치 20마다 레벨1증가) 1

--기능=>함수로구현
밥먹기: #hp 5증가
잠자기: hp 10증가
운동하기: hp 15감소. exp 15증가
놀기:hp 5감소. exp 7증가. hp감소(죽었나?). exp증가(레벨업체크)
종료
'''
hp = 30
exp = 0
lv = 1
while True:
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

print('게임종료')