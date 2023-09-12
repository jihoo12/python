# ## 클래스 class
# # 계산기 프로그램 함수
# result = 0

# def add(n):
#     global result
#     result += n
#     return result

# print(add(10000))
# print(add(5000))

# ## 계산기 프로그램_클래스
# class Money:
#     total = 0

#     def add(self, num):
#         self.total += num
#         return print(f"{self.total}")
# # 클래스 객체 생성    
# income = Money()
# outcome = Money()

# #클래스 사용
# income.add(10000)
# income.add(5000)
# outcome.add(10000)

# ##생성자 #클래스 초기화 메소드(함수)
# class Money:
#     def __init__(self,title):
#         self.total = 0
#         self.title = title
#     def add(self, num):
#         self.total += num
#         return print(f"{self.title} : {self.total}")
# # 클래스 객체 생성    
# income = Money("수입")
# outcome = Money("지출")

# #클래스 사용
# income.add(10000)
# income.add(5000)
# outcome.add(10000)

# # 클래스 상속
# ## 계산기
# class Cal:
#     total = 0
#     def __int__(self):
#         self.total = 0
        
#     def add(self, num):
#         self.total += num
#         return print(self.total)

# class Cal_child(Cal):
#     def sub(self, num):
#         self.total -= num
#         return print(self.total)
#     def add(self, num):
#         self.total += num
#         return print(self.total)
#     def mul(self, num):
#         self.total *= num
#         return print(self.total)
#     def div(self, num):
#         self.total /= num
#         return print(self.total)
# cal1 = Cal()
# cal1.add(10)

# cal2 = Cal_child()
# cal2.add(10)
# cal2.sub(3)
# cal2.mul(4)
# cal2.div(3)
# ## 메서드 오버라이딩
class Cal:
    total = 0
    def __int__(self):
        self.total = 0
        
    def add(self, num):
        self.total += num
        return print(self.total)

class Cal_child(Cal):
    def sub(self, num):
        self.total -= num
        return print(self.total)
    def add(self, num):
        self.total += num
        return print(self.total)
    def mul(self, num):
        self.total *= num
        return print(self.total)
    def div(self, num):
        self.total /= num
        return print(self.total)
    
class Cal_update(Cal_child): #메서드 오버라이딩
    def div(self, num):
        if num == 0: print("잘못된 연산입니다")
        else:
            self.total /= num
            return print(self.total)
        
cal1 = Cal()
cal1.add(10)

cal2 = Cal_update()
cal2.add(10)
cal2.sub(3)
cal2.mul(4)
cal2.div(3)
(f"f(f{f[f(f{f[f(f{f[f(f{f[f(f{f[f(f{f[f(f{f[f(f{f[f(f{f[f(f{f[f(f{f[f(f{f[f(f{f[f(f{f[f(f{f[f(f{f[f(f{f[f({[({[({[({[({[({[({[]})]})]})]})]})]})]})]})]})]})]})]})]})]})]})]})]})]})]})]})]})]})]})]})")