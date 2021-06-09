'''
1. 1-100 소수 출력
2. 크기 입력받아 삼각형 출력
*
**
***
****
크기 입력받아 삼각형 출력
    *
   **
  ***
 ****
*****
크기 입력받아 삼각형 출력
  *
 ***
*****
크기 입력받아 마름모 출력
  *
 ***
*****
 ***
  *
'''

# 1-100 소수 출력
for i in range(1,101):
    for j in range(2,i+1):
        if (j==i):
            print(i)
        elif (i%j==0):
            break
print()
'''
# 크기 입력받아 삼각형 출력
*
**
***
****
'''

for i in range(1,5):
    for j in range(1,i+1):
        print('*', end='')
    print()
print()

i = 3
for j in range(1, i+1):
    print(" "*(i-j), "*"*(2*j-1))
print()

n = int(input('number : '))
for i in range(1, n+1):
    print(" "*(n-i), "*"*(2*i-1))
print()