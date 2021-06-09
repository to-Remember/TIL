def printList(arr):
    for i in arr:
        print(i, end=', ')
    print()

#리스트 요소의 총합 반환 함수
def sumList(x):
    s = 0
    for i in x:
        s += i
    return s

#리스트의 최대값 반환 함수
def maxList(x):
    m = x[0]  #첫 요소를 max값으로 초기화,  리스트 요소와 하나씩 비교하면서 더 큰값을 만나면 바로 m으로 교체
    for i in x:
        if m < i:
            m = i
    return m

#리스트 최소값 반환 함수
def minList(x):
    m = x[0]  #첫 요소를 min값으로 초기화,  리스트 요소와 하나씩 비교하면서 더 작은 값을 만나면 바로 m으로 교체
    for i in x:
        if m > i:
            m = i
    return m

def main():#main함수. 프로그램의 시작점
    a = [1,2,3,4,5]
    printList(a)
    k = sumList(a)
    print('총합:', k)
    max = maxList(a)
    print('max:', max)
    min = minList(a)
    print('min:', min)

    b=[9,8,7,6,6,5,4]
    printList(b)
    k = sumList(b)
    print('총합:', k)
    max = maxList(b)
    print('max:', max)
    min = minList(b)
    print('min:', min)

main()#main호출