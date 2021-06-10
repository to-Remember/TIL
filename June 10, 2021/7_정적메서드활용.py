#정적메서드 및 정적변수 활용 예:
#-> 객체 생성없이 클래스에 제공하는 메서드(기능)를 사용하는 클래스
#API 기능 제공

class Math:
    __pi = 3.14  #변수앞에 __붙이면 private멤버변수이므로 클래스 밖에서 안보임
    PI = __pi  #우회적으로 파이썬에서 상수를 만드는 방법

    def circle(r):
        return r*r*Math.PI

    def rect(w, h):
        return w*h

def main():
    print('pi:', Math.PI)
    w = Math.circle(5)
    print('원의 넓이:', w)
    w = Math.rect(5, 10)
    print('사각형의 넓이:', w)

main()
