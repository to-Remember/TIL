'''
# 번호, 이름, 국, 영, 수, 총, 평
datas={}
num=1 #번호
titles = ['번호','이름','국어','영어','수학','총점','평균']

for i in range(0, 3):
    s = {}
    total = 0
    for j in range(1, 5):
        val = input(titles[j])
        if j!=1: #입력받는게 이름이 아니면
            val = int(val) #문자열 점수를 정수타입으로
            total += val
        s[titles[j]]=val
    s[titles[j+1]]=total
    s[titles[j + 2]] = total/3
    datas[num]=s
    num+=1

print(datas)
'''

# 번호, 이름, 국, 영, 수, 총, 평
datas={}
num=1 #번호
titles = ['번호','이름','국어','영어','수학','총점','평균']

for i in range(0, 3):
    s = {}
    total = 0
    for j in range(1, 5):
        val = input(titles[j])
        if j!=1: #입력받는게 이름이 아니면
            val = int(val) #문자열 점수를 정수타입으로
            total += val
        s[titles[j]]=val
    s[titles[j+1]]=total
    s[titles[j + 2]] = total/3
    datas[num]=s
    num+=1

for i in titles:
    print(i, end='\t')
print()

nums = datas.keys() #nums: [1,2,3]
for i in nums:
    dic = datas[i]
    for key in titles:
        if key=='번호' :
            print(i, end='\t')
        else:
            print(dic[key], end='\t')
    print()