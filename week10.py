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
# num = int(input())
# for i in range(1,num+1):
#     for j in range(num,i,-1):
#         print(' ', end='')
#     print('*' * i)    
# 피라미드출력    
# num = int(input())
# for i in range(1,num+1):
    # for j in range(num,i,-1):
        # print(' ', end='')     
    # print('*' * ((i*2)-1))
### 중간평가 
## 1.
# stri = str(input("str:"))
# num = int(input("int:"))
# print(f"{stri}{num}")

## 2.
# s = "과천코딩2022"
# print(s[2:6])

## 3.
# stri = str(input("str:"))
# num = int(input("int:"))
# print(f"어제 {stri}를 {num}개 먹었습니다.")

## 4.
# num = int(input("int:"))
# num1 = int(input("int:"))
# print(num+num1)
# print(num-num1)
# print(num*num1)
# print(num/num1)

## 5.
# num = int(input("int:"))
# if num % 2 == 0:
#     print("짝수입니다")
# else:
#     print("홀수입니다")

## 6.
# num = int(input("int:"))
# for i in range(1,num+1):
#     if num % i == 0:
#         print(i,end=" ")

## 7.
# num1 = []
# num = int(input("int:"))
# for i in range(1,num+1):
#      if num % i == 0:
#          num1.append(i)
# if len(num1) == 2:
#     print("true")  
# else:
#     print("false")     

## 8.
# num = int(input("int:"))
# for i in range(1,10):
#     print(f"{num}*{i}={num*i}")

## 9.
# num1 = []
# num = int(input("int:"))
# for i in range(1,num+1):
#     num1.append(i)
# print(sum(num1)) 

## 10.
num = int(input("int:"))
for i in range(1, num+1):
    print(i)