# num = int(input("int:"))
# for i in range(1, num+1):
#     if i%3==0 and i < 10:
#         print("x",end=" ")
#     elif str(i).count("3") > 0:
#         print("x",end=" ")
#     elif str(i).count("6") > 0:
#         print("x",end=" ")
#     elif str(i).count("9") > 0:
#         print("x",end=" ")
#     else:
#         print(i,end=" ")

# 11
# num = int(input("int:"))
# for i in range(1,num+1):
#     for j in range(num):
#         print(j+i,end=" ")
#     print("\n")

# 12
# num = int(input("int:"))
# for i in range(num,1,-1):
#     for j in range(num,i,-1):
#         print(' ', end='')     
#     print('*' * ((i*2)-1))
# for i in range(1,num+1,1):
#     for j in range(num,i,-1):5
#         print(' ', end='')     
#     print('*' * ((i*2)-1))

num = int(input("int:"))
for i in range(num*2-1):
    if i < num:
        print(' '*i + '*'*((num-i)*2-1))
    else:
        print(' '*(num*2-i-2) + '*'*((i-num+1)*2+1))