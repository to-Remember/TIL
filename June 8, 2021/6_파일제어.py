'''
1)파일절삭
지정한 크기로 파일 단편화
file.truncate(size)

2)파일명 바꾸기
os.rename(old, new)

3) 파일 삭제
os.remove(파일명)

4)현재 작업디렉토리
  os.getcwd()

5)작업 디렉토리 변경
os.chdir(path)

6)디렉토리 생성
os.mkdir(path)

7)디렉토리 삭제
os.rmdir(path)

8)디렉토리 안에 있는 파일 목록
os.listdir(path)

9)파일 존재 확인
os.path.isfile(path) => 파일 있으면 True, 없으면 False

10)디렉토리 존재 확인
os.path.isdir(path) => 디렉토리 있으면 True, 없으면 False

'''
import os
def trunc():
    file_name = './files/g.txt'
    f = open(file_name, 'w')
    s = 'abcdefghijklmnopqrstuvwxyz'
    f.write(s)
    f.truncate(10)
    f.close()

    f = open(file_name, 'r')
    s = f.read()
    print(s)
    f.close()

def rename():
    os.rename('./files/g.txt', './files/g123.txt')
    with open('./files/g123.txt', 'r') as f:
        print(f.read())
'''  에러
    with open('./files/g.txt', 'r') as f:
        print(f.read())
'''

def file_test():
    print('현재 디렉토리:', os.getcwd())
    if os.path.isdir('test'):
        print('files 디렉토이 있음')
    else:
        print('files 디렉토이 없음')
        os.mkdir('test')

    os.chdir('test') #작업 디렉토리 test로 변경
    print('현재 디렉토리:', os.getcwd())

    fname = ['f1.txt', 'f2.txt', 'f3.txt']
    for i in fname:
        f = open(i, 'w')
        f.write(i+' content')
        f.close()

    files = os.listdir()#test 디렉토리 파일 목록(이름)
    print(files)
    for i in files:
        with open(i, 'r') as f:
            s = f.read()
            print(i, ' : ', s)

    os.remove(files[0])#test 디렉토리에서 f1.txt 파일 삭제

    for i in files:
        if os.path.isfile(i):
            print(i, ' 파일 존재함')
        else:
            print(i, ' 파일 삭제됨')

    os.chdir('../')
    print('현재 디렉토리:', os.getcwd())

def main():
    file_test()

main()
