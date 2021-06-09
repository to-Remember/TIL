'''
<예외발생>
컴파일시 에러: 문법적 에러(한 예로 뒤에 점을 안찍는 행위)
예외: 런타임시 문제 발생
<예외발생>
예외발생 -> 예외 객체를 생성해서 던진다. -> 프로그램이 예외객체를 맞으면 죽어..
<예외처리>
프로그램이 예외객체를 맞아씅ㄹ 때 죽지않게 처리
파이썬에서 예외처리가 필수는 아니지만 프로그램의 안정성을 높이기 위해서 사용하는 것이 좋다

<예외처리 구문>
try - except구문
try:
    예외발생 예측
    (예외발생 가능성 있는 것 여기다 넣기)
    (만약 오류구문 있을 시 밑에 지문 실행 안되고 바로 except구문으로 넘어감)
    (e.g.)res=3/0
except 예외명1: as e: #as e는 발생한 예외 객체를 변수 e에 저장
    예외처리작성
except 예외명2:
    예외처리작성
except Exception as e: #모든 예외 객체를 받음
    예외처리작성
else: #예외가 발생하지 않았을 때 실행되는 블록
    실행문
finally: #무조건 실행되는 블록
    실행문


'''

def main():
    print('프로그램 시작')
    arr = [1,2,3]
    try:
        #arr[3]=4
        #res = 3 / 0
        print('test1')
        res='aaa' + 1
        print('test2')
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print('예외가 발생했지만 위 except에서 잡지 못하면 여기로 온다')
    else:
        print('예외가 발생하지 않았음')
    finally:
        print('예외가 발생하건, 정상 실행되건 종료전 항상 실행되는 블록')

    print('프로그램 종료')

main()
