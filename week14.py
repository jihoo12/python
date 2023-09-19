# # ## 내장모듈

# # ## 타이머 프로그램
# # import time

# # sec = int(input("시간초 입력:"))

# # for i in range(sec, 0, -1):
# #     print(i)
# #     time.sleep(1)
# # print("타이머종료")
# ### turtle
# import turtle
# # 스크린 생성
# turtle.setup(width=600, height=600)
# t = turtle.Turtle()
# t.shape("turtle")
# # for i in range():
# #     t.forward(100)
# #     t.left(72)
# def shape(n,m,b):
#     for i in range(n):
#         t.speed(b)
#         t.forward(m)
#         t.left(360/n)
# shape(int(input()),int(input()),int(input()))
# turtle.exitonclick()
import move
import attack
p1 = attack.Attack('검사')
p1.sword()
move.down()