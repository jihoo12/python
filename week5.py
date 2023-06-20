# # # fruits = ['사과','망고','바나나','수박','멜론']

# # # # print(fruits)
# # # # print(fruits[0])
# # # # print(fruits[2])

# # # # #.join()
# # # # print('\n'.join(fruits))

# #l1 = [1,2,3,4,5]
# # # l2 = l1[:] #l1전채
# # # l2.copy(l1)
# # print(l1==l2)
# # print(l1 is l2)
# # print(l1)
# # print(l2)
# # l2[0] = 5
# # print(l1)
# # print(l2)

# # print(l1)
# # print(l1[::-1]) #역순

# # *표현식
# # *a, b, c = l1
# # print(a,b,c)

# # a, *b, c = l1
# # print(a,b,c)

# # a, b, *c = l1
# # print(a,b,c)

# ###중첩리스트
# # ll = [
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9]
# # ]
# # print(ll)
# # print(ll[0])
# # print(ll[1][1])

# ## 중첩 리스트 활용
# # level = [1,2,3,4,5]
# # weapon = ['맨손','목검','청동검','철검','명검']
# # armor = ['장갑','전투화','투구','갑옷','망토']

# # item = [level,weapon,armor]
# # print(item)
# # print(item[0][0], item[1][0], item[2][0])
# # print(item[0][1], item[1][1], item[2][1])
# # print(item[0][3], item[1][3], item[2][3])

# # 학생 명부 만들기 
# # 학생명부 = [
# #     ['지후'],
# #     ['남자'],
# #     ['010-1234-5678']
# # ]
# # print(학생명부)
# # s = input("학생정보입력").split()
# # print(s)
# # 학생명부[0].append(s[0])
# # 학생명부[1].append(s[1])
# # 학생명부[2].append(s[2])

# # print(학생명부)

# ### 튜플
# # t1 = (1,2,3)
# # t2 = (4,5,6)
# # print(t1, type(t1))
# # print(t2, type(t2))
# # print(t1+t2)
# # print(t1 * 3)
# # print(t1[0:2])
# # print(t1[::-1])

# # t1 = (1,2,3,4,5)
# # t2 = t1[:] #l1전체 복사
# # # t2.copy(t1)
# # print(t1==t2)
# # print(t1 is t2)
# # print(t1)
# # print(t2)
# # # l2[0] = 5
# # print(t1)
# # print(t2)

# ##zip() : 같은 크기로 이루어진 자료형들을 묶는함수 (튜플로)
# n1 = [1,2,3,4,5,6]
# c1 = ['a','b','c','d','e']
# # z = list(zip(n1, c1))
# z = tuple(zip(n1, c1))

# print(z, type(z))