# # ### 포멧팅
# # name = "박지후"
# # age = 17
# # height = 170.5
# # # print("이름:",name,age)
# # #포멧기호
# # print("이름: %s, 나이: %d, 키: %.2f" %(name, age, height))
# # #format() 사용
# # print("이름: {}, 나이: {}, 키: {:.2f}".format(name, age, height))

# # #f-string 사용
# # print(f"이름: {name}, 나이: {age:.2f}, 키: {height:.2f}")

# ### 리스트
# #예
# # text = "hello_world"
# # text = text.split()
# # print(type(text))

# # ## 리스트 만들기
# # gimbab = ['김', '밥', '치즈', '스팸', '단무지']
# # print(gimbab)
# # print(gimbab[2:])

# # ##내 정보 리스트 만들기
# # info = ["박지후",17,170.5,"중앙고"]
# # print(info)
# # print(f"이름: {info[0]}, 나이: {info[1]}, 키: {info[2]}, 학교: {info[3]}")

# ### 리스트 함수

# # score = [90, 80, 100, 70]
# ##파이썬 기본 함수
# # print(max(score)) #최대값
# # print(min(score)) #최소값
# # print(len(score)) #길이반환
# # print(sum(score)) #값들의 합 반환

# # print(sum(score)/len(score))

# ## 리스트에서 활용할수있는 함수(메소드) 추가 삭제 
# # fruits = ['사과', '바나나', '수박', '포도']
# # print(fruits)
# # #추가
# # fruits.append('멜론')
# # print(fruits)
# # fruits.insert(2,"망고")
# # print(fruits)

# # #삭제
# # fruits.pop() #리스트맨마지막 값 삭제
# # print(fruits)
# # fruits.remove("사과")
# # print(fruits)

# student = ['지후', '뽀로로', '포비']
# new_student = ['타요','스쿨비']

# print(student+new_student)
# student.extend(new_student)
# print(student)

## 리스트 정보
# st = ['지후', '뽀로로', '포비']
# print(st.index('뽀로로'))#해당갑의 인데스 반환
# print(st.count('뽀로로'))#해당값의갯수
##리스트 정렬
score = [90, 80, 100, 70]

print(score)
score.reverse()#역순
print(score)
score.sort()#오름차순 정렬
print(score)
score.sort(reverse=True)
print(score)
