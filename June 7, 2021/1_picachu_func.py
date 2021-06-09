'''
def main():
#기본 시작점 지정을 이렇게 많이 함
1) if __name__ == '__main__':  ##def main(): #프로그램 시작 함수
2) def main(): -->  print(__name__)
# pass: #함수나 클래스 구현을 나중으로 미루고 비워둘 때 사용
'''
# 라마메터 받아서 하는 방법 (전역변수로 하면 파라메터 필요없음)
#피카추 게임
def 밥먹음(hp_val):
    print('피카추 밥먹음')
    hp_val += 5
    return hp_val

def 잠잠(hp_val):
    print('피카추 잠잠')
    hp_val += 10
    return hp_val

def 놀기(hp_val, exp_val, lv_val):
    print('피카추 논다')
    hp_val -= 8
    flag = hp_val>0
    if flag:
        exp_val += 5
        if exp_val >= 20: #경험치가 20 채워졌나?
            lv_val += 1 #채워졌다면 레벨 1증가
            exp_val -= 20 #경험치 20감소
            print('레벨 1 상승')
    return hp_val, flag, exp_val, lv_val #파이썬은 여러개의 값 반환 가능. 튜플로 반환
                 # 비교연산의 결과는 True/False  --> 밑에 flag로 연결

def 운동하기(hp_val, exp_val, lv_val):
    print('피카추 운동함')
    hp_val -= 15
    flag = hp_val > 0
    if flag:
        exp_val += 10
        if exp_val >= 20:  # 경험치가 20 채워졌나?
            lv_val += 1  # 채워졌다면 레벨 1증가
            exp_val -= 20  # 경험치 20감소
            print('레벨 1 상승')
    return hp_val, flag, exp_val, lv_val

def printInfo(hp_val, exp_val, lv_val):
    print('캐릭터 상태')
    print('hp: ', hp_val)
    print('exp: ', exp_val)
    print('lv: ', lv_val)

def main():
    hp = 30 #지역변수(함수 안에서 선언)
    exp = 0
    lv = 1
    flag = True
    while flag:
        menu = input('1.밥먹기 2.잠자기 3.운동하기 4.놀기 5.상태확인 6.종료')
        if menu == '1':
            hp = 밥먹음(hp) #앞에 hp랑 뒤에 파라메터 있어야지 변경된 값이 리턴됨
        elif menu == '2':
            hp = 잠잠(hp)
        elif menu == '3':
            hp, flag, exp, lv = 운동하기(hp, exp, lv)  #flag=false캐릭터 죽을때 루프를 빠져나감
            #x=운동하기(hp)
            #x[0]=hp
            #x[1]=flag
        elif menu == '4':
            hp, flag, exp, lv = 놀기(hp, exp, lv)
        elif menu == '5':
            printInfo(hp, exp, lv)
        elif menu == '6':
            print('게임종료')
            break
        if not flag:
            print('캐릭터 사망')



main()   #main() 이랑 똑같은거