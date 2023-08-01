### 반복문 - for
#for*list
# students = ['pororo','krong','phobe']
# num = 0
# for student in students:
#     # num += 1
#     # print(num)
#     print(student)
#for*tuple
# score_tuple = (100,80,90,70)

# for score in score_tuple:
#     print(score, end=' ')
#for*string
# text = "Hello, world"

# for l in text:
#     print(l)
#for*dictionary
# score = {'math':90,'english':100,'Science':70,'history':80}

# for sub in score:
#     print(f"{sub} : {score[sub]}점")
#for*range()
#숫자생성
# num_list = list(range(1,11,2))
# print(num_list)
# for i in range(1,101):
#     print(i,end='')
###구구단 출력
# number = int(input())
# for i in range(1,10):
#     print(f"{number}*{i}={number*i}")

### continue : 명령 건너뛰기
number = []
for i in range(1, 101):
    number.append(i)
    
for i in number:
    if i % 2 == 0:
        print("짝수")    
    else:
        print(i)
        continue    
        print("홀수")
        
# n줄만큼 삼각형출력 
'''       
11111
22222
33333
44444
55555`
'''
