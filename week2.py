# print(type(10))#int: 정수형 자료형, integer
# print(type(10.5))#float: 실수형 자료형,소수점을 가진숫자
# print(type(10+5))
# print(type('안녕')) #str: 문자열 자료형, string

# ### 연산자
# print(10+5,type(10+5))
# print(10-5,type(10-5))
# print(10*5,type(10*5))
# print(10/5,type(10/5))#나누기 연산의 결과는 실수(float)로저장됨
# print(int(10/5),type(int(10/5)))
# print(float(10*5),type(float(10*5)))
# print(str(10*5),type(str(10*5)))

# print(10/3)#나눗셈
# print(10//3)#몫
# print(10%3)#나머지


# print(10**10)# 제곱근

###변수
# number = 10
# print(number*2, type(number*2))
# name = "지후"
# print(name, type(name))

#복합대입연산자
# num1 = 10
# num2 = 5

# # num1 = num1+num2
# num1 += num2
# print(num1)
# num1 -= num2
# print(num1)
# num1 *= num2
# print(num1)
# num1 /= num2
# print(num1)

##비교연산자
# a = 10
# b= 20

# print(a!=b)
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)

## 논리연산
# a=10
# b=20
# #and(논리곱) : 둘다 true인경우만 true반환
# print(a==10 and b==20)#true
# print(a!=10 and b==20)#false
# print(a==10 and b!=20)#false
# print(a!=10 and b!=20)#false

# #or(논리합) : 둘다 false인경우만 false반환
# print(a==10 or b==20)#true
# print(a!=10 or b==20)#true
# print(a==10 or b!=20)#true
# print(a!=10 or b!=20)#false

# ##not연산 반대의 값반환
# print(not a==b) #true
# print(not a!=b) #false
# print(not 0) #true 0은 항상 False(거짓)
# print(not 1) #false 0이아닌 모든것값은 true(참)

### 사용자입력함수
## input함수는 항상 문자열로 저장
name = input("Enter you are name") 

print(name, type(name))

age = int(input("how old are you"))
print(age, type(age))

