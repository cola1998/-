# B1011 A+B和C
# T = int(input())
# for i in range(0,T):
#     l = input().split(' ')
#     if (int(l[0])+int(l[1])>int(l[2])):
#         print("Case #{0}: true".format(i+1))
#     else:
#         print("Case #{0}: false".format(i+1))

#B1016 部分A+B
# L = input().split(' ')
# Da = int(L[1])
# Pa = 0
# A = list(L[0])
# for i in range(len(A)):
#     if int(A[i]) == Da:
#         Pa = Pa*10 + Da
#
# Db = int(L[3])
# Pb = 0
# B = list(L[2])
# for i in range(len(B)):
#     if int(B[i]) == Db:
#         Pb = Pb*10 + Db
# print(Pa+Pb)

#B1026 程序运行时间
# l = input().split(' ')
# C1 = int(l[0])
# C2 = int(l[1])
# CLK_TCK = 100
# time_s = int((C2 - C1 + 50)/CLK_TCK)
# time_h = int(time_s//3600)
# time_m = int((time_s%3600)//60)
# time_s = (time_s%3600)%60
# print("%02d:%02d:%02d"%(time_h,time_m,time_s))

#B1046 划拳
# failA = 0
# failB = 0
# N = int(input())
# for i in range(N):
#     l = input().split(' ')
#     a1 = int(l[0])
#     a2 = int(l[1])
#     b1 = int(l[2])
#     b2 = int(l[3])
#     if (a1 + b1 == a2) and (a1 + b1 != b2):
#         failB += 1
#     elif (a1 + b1 == b2) and (a1 + b1 != a2):
#         failA += 1
# print("{0} {1}".format(failA,failB))

#1008 数组元素循环右移
# l = input().split(' ')
# N = int(l[0])
# M = int(l[1])
# M = M%N  #修正M !!
# l = input().split(' ')
# for i in range(len(l)):
#     if (len(l)-M+i) <= len(l)-1:
#         print('{0} '.format(l[len(l)-M+i]),end='')
#     else:
#         if (i==len(l)-1):
#             print('{0}'.format(l[i - M]))
#         else:
#             print('{0} '.format(l[i-M]),end='')

#B1012 数字分类
# import math
# l = input().split(' ')
# num_list = [0,0,0,0,0]
# A2_n,A3_n = 1,0
# N = int(l[0])
# for i in range(1,len(l)):
#     x = int(l[i])
#     if (x%5 == 0 and x%2==0):
#         num_list[0] += x
#     elif (x%5 == 1):
#         A2_n += 1
#         num_list[1] += int(math.pow(-1,A2_n)*x)
#     elif (x%5 == 2):
#         num_list[2] += 1
#     elif (x%5 == 3):
#         A3_n += 1
#         num_list[3] += x
#     elif (x%5 == 4):
#         if(num_list[4] < x):
#             num_list[4] = x
# if (A3_n != 0):
#         num_list[3] = round(num_list[3]/A3_n,1)
# for i in range(len(num_list)):
#     if i==(len(num_list)-1):
#         if (num_list[i] == 0):
#             print('{0}'.format('N'))
#         else:
#             print("{0}".format(num_list[i]))
#     else:
#         if (num_list[i] == 0):
#             if (i == 2 and A2_n!=0):
#                 print('{0} '.format(num_list[i]), end='')
#             else:
#                 print('{0} '.format('N'), end='')
#         else:
#             print('{0} '.format(num_list[i]),end='')

#B1018
N = int(input())
a = [0,0,0]  #存储甲的胜平负次数
b = [0,0,0]  #存储乙的胜负平次数
a_dict = {'B':0,'C':0,'J':0} #存储胜利的次数
b_dict = {'B':0,'C':0,'J':0}

for i in range(N):
    l = input().split(' ')
    #0是甲 1是乙
    if(l[0] == 'C'):
        if(l[1] == 'B'):
            a[2] += 1
            b[0] += 1
            b_dict['B'] += 1
        elif (l[1] == 'J'):
            a[0] += 1
            b[2] += 1
            a_dict['C'] += 1
        else:
            a[1] +=1
            b[1] += 1
    elif (l[0] == 'J'):
        if (l[1] == 'C'):
            a[2] += 1
            b[0] += 1
            b_dict['C'] += 1
        elif (l[1] == 'B'):
            a[0] += 1
            b[2] += 1
            a_dict['J'] += 1
        else:
            a[1] += 1
            b[1] += 1
    elif (l[0] == 'B'):
        if (l[1] == 'J'):
            a[2] += 1
            b[0] += 1
            b_dict['J'] += 1
        elif (l[1] == 'C'):
            a[0] += 1
            b[2] += 1
            a_dict['B'] += 1
        else:
            a[1] += 1
            b[1] += 1

for i in range(3):
    if i == 2:
        print("{0}".format(a[i]))
    else:
        print("{0} ".format(a[i]),end='')
for i in range(3):
    if i == 2:
        print("{0}".format(b[i]))
    else:
        print("{0} ".format(b[i]),end='')
print("{0} {1}".format(max(a_dict,key=a_dict.get),max(b_dict,key=b_dict.get)))