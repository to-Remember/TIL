'''
1. 예외 클래스 만들 수 있음. 파이선에 정의되지 않은 예외 클래스 쓰고 싶을 때 직접 만들어서 사용.
class 예외클래스명(Exception):
    def__init__(self,msg): #생성자. 객체 초기화 함수. 사용할 에러 메시지 할당
        self.msg = msg

2. 예외 발생 시킴 -> 파이선이 인지하지 못하는 예외를 직접 발생시키고 싶을 때 사용
raise 예외객체 생성

3. 함수에서 예외가 발생하면 먼저 그 함수 안에서 예외처리 코드를 찾고 있으면 그것을 실행
없으면 이 함수를 호출한 위치에서 예외처리 구문을 또 찾음 (스택언롤링)
있으면 그 예외처리 구문을 실행없고 없으면 다운. 프로그램 중단.
'''


class NumError(Exception):
    def __init__(self, msg): #생성자. 객체 초기화 함수
        self.msg = msg

def f1(num): #5이하의 숫자만 가능. 5보다 큰 숫자를 받으면 심각한 발생
    if num > 5:
        raise NumError('num은 5보다 작거나 같아야 함')

    print(num)

def f2(mum):
    if not isinstance(num, int): #a의 타입이 type이냐? 맞으면 True, 아니면 False
        raise TypeError('num은 int이어야 함')
    return num+10

def main():
    try:
        f1(10)
        f1(4)
        f2('asdf')
    except NumError as e:
        print(e.msg)
    except TypeError as e:
        print(e)

main()
