# ### 숙제
# number = int(input())
# # for i in range(number+1):
# #     print("*" * i)
# for i in range(number+1):
#     print(str(i) * number)
### for 활용
#Q. 두 개의 숫자를 입력받아서, 두 숫자사이의 수 출력
# num1 = int(input())
# num2 = int(input())
# for i in range(num1,num2+1):
#     print(i, end=' ')
# num = input().split()
# # num1 = []
# # for i in num:
# #     num1.append(int(i))
# # print(num1)
# num1 = [int(i) for i in num]
# print(num1)
# num = [int(i) for i in input().split()]
# print(sum(num))
### 중첩 for문
num = int(input())
for i in range(1,num+1):
    for j in range(num,i,-1):
        print(' ', end='')
    print('*' * i)    
###피라미드출력    