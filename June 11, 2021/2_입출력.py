'''


오픈모드 (r,w,a-읽기,쓰기,이어쓰기)
'''
import os
import sys
def stdTest():
    msg = sys.stdin.readline(10)
    sys.stdout.write('msg:'+msg+'\n')
    sys.stderr.write('에러 메시지 출력\n')
    sys.stderr.write('에러 메시지 출력\n')

def fileRead(path):
    try:
        f = open(path, 'r', encoding='utf-8')
        x = f.read() #파일읽기. 파일에서 읽은 내용 반환. -> 변수 ㅌdp wjwkd
        print(x)
        f.close()

    except Exception as e:
        print(e)

def filewrite(path, msg):
    try:
        f = open(path,'w',encoding='etf-8') #쓰기모드 파일 오픈
        f.write(msg)
        f.close()
    except Exception as e:
        print(e)

def printDirList(path):
    if os.path.isdir(path):

    fname = os.listdir(path) #path 폴더에 있는 모든 파일이나 디렉토리 이름(문자열)을 모두 읽어서 리스트에 담아서 반환
                             #path가 10day: ['a.txt', 'b.txt', '입출력.py', '패키지호출예.py']
    for file in fname:
        print(file)


def main():
    #stdTest()
    filewrite('b.txt', 'hello file\n')
    fileRead('b.txt')


main()