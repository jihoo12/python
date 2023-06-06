# ###string
# fruit1 = "수박"
# fruit2 = "사과"
# # print(fruit1)
# # print(fruit2)
# print(fruit1, fruit2,sep='')
# print(fruit1, fruit2)
# print(fruit1, end='')
# print(fruit2)

# ###문자열 연산
# print(fruit2 + fruit1)#병합
# print(fruit2 - fruit1)
# print(fruit2 * 1)
###인덱스(index)
# hi = 'hello world'
# print(hi[0])
# print(hi[6])
# print(hi[-11])
# print(hi[-5])

# a = "abcdefghijklmnopqrstuvwxyz"
# name = a[9]+a[8]+a[7]+a[14]+a[14]
# print(name)

###인덱스 슬라이싱
# word = "butterfly"
# print(word[0:6])
# print(word[-3:])
# print(word[6:9])

text = "\t\"There is no one \\who loves pain itself, \nwho seeks after it and wants to have it, simply because it is pain...\""

# # print(text)

# ###문자열함수
# print(text.count('who')) #특정문자의개수반환
# print(text.count('e'))

# print(text.upper())#문자열 대문자로 변환
# print(print(text.lower()))

# print(text.replace('who', 'that'))#문자열 치환
# print(len(text))#문자열 길이반환

# print(text.replace(' ', '\n'))#문자열 치환

# print(len(text.replace(" ", "")))#문자열 길이반환


# text2 = text.split()
# print(text2, type(text2))

# num = "010-1234-5678"
# print(num.isdigit())
# num = num.replace("-", "")
# print(num.isdigit())
# print(num.isalpha())

# id = "jake1"
# print(id)
# print(id.isalpha())
# id = id.replace('1', '')
# print(id.isalpha())

###exercise
# #1. 두개의 문자열을 입력 받아서, 한줄로 출력
# t1 = input("문자열1:")
# t2 = input("문자열2:")
# print(t1+t2)
# print(t1, t2, sep='')
# print(t1, end='')
# print(t2)
#2. 공백이있는 하나의 문자열을 입력받아서 두줄로 출력
text = input()
text = text.replace(" ", "\n")
print(text)
text = text.split()
print(text[0],text[1], sep='\n')
