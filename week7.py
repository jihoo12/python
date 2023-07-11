# # # # # # # # # ### 제어문
# # # # # # # # # ## 조건문 if

# # # # # # # # # case = 1
# # # # # # # # # if case:#case == True:
# # # # # # # # #     print("조건이 참 = 실행")

# # # # # # # # num = int(input("숫자 입력: "))

# # # # # # # # if num>10:
# # # # # # # #     print("입력한숫자는10보다큽니다")
# # # # # # # # elif num < 10:
# # # # # # # #     print("입력한숫자는 10보다잓ㅡㅂ니다")
# # # # # # # # else:
# # # # # # # #     print("입력한 숫자는 10입니다")

# # # # # # # ### 조건문 연습
# # # # # # # #Q. 하나의 숫자를 입력받아서, 그 숫자가 홀수인지 짝수인지 출력
# # # # # # # num = int(input("숫자 입력: "))
# # # # # # # num1 = num%2
# # # # # # # if num1==0:
# # # # # # #     print("짝수")
# # # # # # # else:
# # # # # # #     print("홀수")    
    
# # # # # # ## 삼항연산자
# # # # # # # (항1) 조건 (항2) 조건 (항3)
# # # # # # a = 10
# # # # # # print("짝수") if a % 2 ==0 else print("홀수")

# # # # # ## 중첩 if
# # # # # # num = int(input("숫자 입력: "))

# # # # # # if num>10:
# # # # # #     print("입력한숫자는10보다큽니다")
# # # # # #     if num % 2 == 0: print("짝수입니다")
# # # # # #     else: print("홀수입니다")
# # # # # # elif num < 10:
# # # # # #     print("입력한숫자는 10보다작습니다")
# # # # # #     if num % 2 == 0: print("짝수입니다")
# # # # # #     else: print("홀수입니다")
# # # # # # else:
# # # # # #     print("입력한 숫자는 10입니다. \n짝수입니다")

# # # # # ## 조건문과 논리연산
# # # # # num = int(input("숫자 입력: "))

# # # # # if num>10 and num % 2 == 0:
# # # # #     print("입력한숫자는10보다큽니다\n짝수입니다")
# # # # # elif num>10 and num % 2 == 1:
# # # # #     print("입력한숫자는10보다큽니다\n홀수입니다")
# # # # # elif num<10 and num % 2 == 0:
# # # # #     print("입력한숫자는10보다작습니다\n짝수입니다")
# # # # # elif num<10 and num % 2 == 1:
# # # # #     print("입력한숫자는10보다작습니다\n홀수입니다")    


# # # # ## 조건문과 멤버십연산자 in
# # # # member = ['뽀로로','에디','크롱']
# # # # friend = input("친구이름: ")

# # # # if friend in member:
# # # #     print(f"{friend}는 내 친구 입니다")
# # # # else:
# # # #     print(f"{friend}는 내 친구가 아닙니다")    

# # # ### 연습문제
# # # ##1. 정수를 여러게 입력 받아서 큰 수와 작은 수를 차례러 출력하는 프로그램을 작성하시오.
# # # number = int(input("정수: "))
# # # number1 = int(input("정수: "))
# # # if number > number1:
# # #     print(number,number1)
# # # else:
# # #     print(number1,number)    
# # ##2. 성적 출력프로그램
# # number = int(input("점수: "))
# # if number >= 90:
# #     print("A")
# # elif number >= 80:
# #     print("B")
# # elif number >= 70:
# #     print("C")
# # else:
# #     print("F")            
# members = ['Tommy','Marry','jake1234']
# ID = input("id: ")
# if ID not in members and len(ID) > 5:
#     print("가입이가능합니다")
#     members.append(ID)    
# print(members)    
'''
BMI비만도계산공식(몸무게/키의제곱)
18.5이하면 저체중
18.5 ~ 22.9 사이먼 정상
23.0 ~ 24.9 사이먼 과체중
25.0이상 비만
'''