# ### Dictionary

# # id = ['jihoo','17','']
# id = {'이름':'jihoo','나이':17,'키':168,'학교':'gcjh'}

# print(id, type(id))

# score = {"영어":100,"수학":80,"국어":90,'역사':100}
# print(score)

# print(score["영어"])
# ## 딕셔너리는 추가와 수정이 동일
# score['체육'] = 100 #기존 키값이 없으면, 추가
# print(score)
# score['역사'] = 70 #기존 키값이 있으면, 수정
# print(score)

# ## 딕셔너리 삭제
# del score['체육']
# print(score)

##딕셔너리 실습
fruits = {'apple':500,'banana':2500,'mango':2000}

# print("망고는 1개당"+fruits['mango']+"원 입니다")
# print(f"망고는 1개당",fruits['mango'],"원 입니다")
# print('망고는 1개당 %d 원 입니다' %fruits['mango'])
# print("망고는 1개당: {}원 입니다".format(fruits['mango']))
# print(f"망고는 1개당 {fruits['mango']}원 입니다")
# fruits['apple'] = 700
# fruits['orange'] = 1500
# del fruits['banana']
# print(fruits)

## 딕셔너리 함수
#key들을 묵어서 반환
print(fruits.keys())
print(list(fruits.keys()))
#value들을 묵어서 반환
print(fruits.values())
print(tuple(fruits.values()))
#key와 value의 쌍으로 묵어서 반환
print(fruits.items())
print(list(fruits.items()))

#특정 key에 해당하는 value반환 없으면 None반환
print(fruits.get('orange'))
print(fruits.get('apple'))

#여러 추가/수정 한 번에 처리
fruits.update({'apple':700,'orange':1500,'watermelon':15000})
print(fruits)

#딕셔너리 초기화
fruits.clear()
print(fruits)
