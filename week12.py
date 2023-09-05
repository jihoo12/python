# ## function 함수
# # 구구단 출력 프로그램
# for i in range(1,10):
#     print(f"2 X {i} = {2*i}")
# 구구단 출력 함수
# def multable(num):
#     for i in range(1,10):
#         print(f"{num} X {i} = {2*i}")

# multable(2)

# # 함수의 형태
# 1.매개변수와반한값이 없는 경우
# def namecard():
#     print("이름:제이크")
#     print("연락처:010-1111-1111")
# namecard()
# 2.매개변수만 있는 경우
# def namecard(name):
#     print(f"이름: {name}")
#     print("연락처:010-1111-1111")
# namecard(input("이름:"))
# 3.반환값만 있는경우
# def namecard():
#     print("이름:제이크")
#     print("연락처:010-1111-1111")
#     return "명함프로그램"
# print(namecard())
# 4.매개변수와반한값이 모두 있는 경우
# def namecard(name):
#     print(f"이름: {name}")
#     print("연락처:010-1111-1111")
    
#     return "과천코딩"
# print(namecard(input("이름:")))
##응용
# cnt = 0
# def namecard(name):
#     global cnt
#     cnt += 1
#     print(f"이름: {name}")
#     print("연락처:010-1111-1111")
    
#     return f"{cnt}과천코딩"
# print(namecard(input("이름:")))
# print(namecard(input("이름:")))
# cnt = 0
# def namecard(*name):
#     global cnt
#     cnt += 1
#     print("==============================================================")
#     for i in name:
#         print(f"{name[i]}")
#     print("==============================================================")
#     return f"{cnt}과천코딩"
# print(namecard("제이크","010-1111-0000","jworks@gmaeil.com","과천코딩"))
# # print(namecard(input("이름:"),input("연락처:")))
# def 원(info):
#     return info*info*3.141592
# def 사각형(w,h):
#     return w*h
# def 삼각형(w,h):
#     return w*h/2
# print(원(int(input())))
# print(사각형(int(input()),int(input())))
# print(삼각형(int(input()),int(input())))
## 외장함수
#import math
# import time
# print(time.time())
# print(time.localtime())
# #print(math.gcd(2,3,5,7,11,13,17,23,29))
import random
print(random.randbytes(1))
rnum = [1,2,3,4,5]
random.shuffle(rnum)
print(rnum)
print(random.choice(rnum))
print(random.sample(rnum,1))
print('\\4d')