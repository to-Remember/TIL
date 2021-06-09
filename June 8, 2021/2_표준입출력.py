#C:\Users\Playdata\PycharmProjects\pythonProject\7day\files\a.txt
#학습목표
#입출력: 입력/출력
#예외처리: 예외 발생시 프로그램이 중단되는 것을 막아 안정성 높임
'''
입출력
입력:데이터가 외부에서 프로그램 방향으로 흘러옴
출력: 데이터가 프로그램에서 외부로 흘러나감

1. 표준입출력(stdio)
기본 제공 입출력
sys.stdin:표준입력
sys.stdout:표준출력
sys.stderr:표준에러
'''

import sys

def main():
    sin = sys.stdin  #키보드 입력 스트림. 스트림:데이터의 흐름을 소프트웨어로 구현한 것
    sout = sys.stdout  #콘솔 출력 스트림
    serr = sys.stderr   #콘솔에 에러 출력 스트림

    num = sout.write('문자를 입력하시오\n')#write():출력 스트림에 출력
    sout.write(str(num)+' 개의 문자 출력됨\n')
    s = sin.read(5)#read(size):입력 스트림에서 size만큼 읽음
    sout.write('입력받은 값:'+s+'\n')
    sout.write('한줄을 입력하시오\n')
    sin.readline()
    s = sin.readline()
    sout.write('입력받은 값:' + s + '\n')
    serr.write('에러 메시지')

main()
