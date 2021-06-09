'''
<다차원 리스트>
다차원 리스트는 복잡한 구조의 데이터를 표현하기 위해 사용
리스를 요소로 갖는 리스트


a = [[1,2,3], [4,5,6]]

print(a[0])#[1,2,3]
print(a[1])#[4,5,6]

print(a[0][0])#1
print(a[0][1])#2
print(a[0][2])#3
print(a[1][0])#4
print(a[1][1])#5
print(a[1][2])#6


for i in a:#2번 반복  방이 2개 짜리 리스트
    for j in i:#[4,5,6]
        print(j, end=',')
    print()

for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        print(a[i][j], end=',')
    print()

for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        a[i][j] *= 10 # a[i][j] = a[i][j] * 10

for i in a:#2번 반복  방이 2개 짜리 리스트
    for j in i:#[4,5,6]
        print(j, end=',')
    print()

#요소 입력받아 저장
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        a[i][j]=int(input('num:'))

print(a)

성적처리 프로그램
3명의 번호, 국, 영, 수 입력받아 각 학생의 총점, 평균 계산해서 결과 출력

번호  국어  영어  수학 총점   평균
1     98    89  87  257     332
2     98    89  87  257     332
3     98    89  87  257     332



# 1. 한 사람의 번호, 국, 영, 수 입력받아 각 학생의 총점, 평균 계산해서 결과 출력
#person = [1, 65, 87, 67, 0, 0]
person = [0]*7 #
#person[4] = person[1]+person[2]+person[3]

title = ['번호', '이름', '국어', '영어', '수학', '총점', '평균']
for i in range(0, 5):
    if i==1:
        person[i] = input(title[i])
    else:
        person[i] = int(input(title[i]))
        if i!=0:
            person[5] += person[i]

person[6]=person[5]/3

for i in title:
    print(i, end='\t')
print()
for i in person:
    print(i, end='\t')
print()
'''
##########################################
score = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
title = ['번호', '국어', '영어', '수학', '총점', '평균']
for i in range(0, 3):#사람수. i는 줄번호
    for j in range(0, 4):#각 사람이 입력 받을 값의 수, j는 각 줄의 칸번호
        score[i][j] = int(input(title[j]))
        if j!=0:
            score[i][4] += score[i][j]

    score[i][5] = score[i][4]/3

print(score)
