###반복문
# cut = 0

# while cut  < 10: #조건이 참일동안 반복
#     cut += 1
#     print(f"나무를 {cut}번 찍었습니다")
# print("나무가넘어갑니다")     

## while 연습
#q1. 정수를 입력받아서 1부터 출력하는 프로그램을 작성하시오
# i = int(input())
# i1 = 0
# while i1 < i:
#     i1 += 1
#     print(i1)

###로그인 프로그램
# member = ['Pororo','krong','phobee']
# number = 0
# while number < 3:
#     number += 1
#     id = input("id:")
#     if id in member:
#         print(f"{id}님, 환영합니다")
#         break
#     else:
#         print("아이디를 확인해주세요.")
        
#무한루프
# play = 10
# roof = True
# # while roof: #무한루프 예 3
# while True: #무한루프 예 4
#     print("게임 실행중")
            
### while 연습 2
#Q. 정수를 입력 받다가 0이 입력되면
# 그 때까지 입력 받은 홀수의 개수와 짝수의 개수를 출력하는 프로그램을 작성하시오
# even = 0
# odd = 0
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1  
# print(f"짝수:{even},홀수:{odd}")

### 별 찍기
# star = 0
# while True:
#     star += 1
#     if star > 5:
#         break
#     print("*" * star)

###숙제
#Q 0부터100까지정수계속입력
# 범위를 넘어가면 정수의 합ㅖ와 평균을 출력
#평균 소수첫째