#codeup 1928  显示答案错误
# import time
# import datetime
#
# def calculateDay(date1,date2):
#     if(date1>date2):
#         temp = date1
#         date1 = date2
#         date2 = temp
#     date1 = time.strptime(date1,"%Y%m%d")
#     date2 = time.strptime(date2,"%Y%m%d")
#     date1 = datetime.datetime(date1[0],date1[1],date1[2])
#     date2 = datetime.datetime(date2[0],date2[1],date2[2])
#     day = date2-date1
#     return day.days+1
#
# d1 = input()
# d2 = input()
# day = calculateDay(d1,d2)
# print(day)

# B1022
# l = input().split(' ')
# D = int(l[2])
# N = int(l[0])+ int(l[1])
# # 求A+B的D进制数
# ll = []
# if(N == 0):
#     print(0)
# else:
#     while N>=D:
#         ll.append(N%D)
#         N = int(N/D)
#     ll.append(N%D)
#     for i in range(len(ll)-1,-1,-1):
#         print(ll[i],end='')

#B1037
#应付P 实付A  得出找的零钱
#规则 17Sickle = 1Galleon 29Knut = 1Sickle
# l = input().split(' ')
# P = list(map(int,l[0].split('.')))
# A = list(map(int,l[1].split('.')))
# Pn = P[0]*17*29+P[1]*29+P[2]
# An = A[0]*17*29+A[1]*29+A[2]
# if An<Pn:
#     resultn = Pn - An
#     print("-{0}.{1}.{2}".format(int(resultn / (17 * 29)), int((resultn % (17 * 29)) / 29), (resultn % (17 * 29)) % 29))
# else:
#     resultn = An-Pn
#     print("{0}.{1}.{2}".format(int(resultn/(17*29)),int((resultn%(17*29))/29),(resultn%(17*29))%29))

#A1019
# l = input().split(' ')
# D = int(l[1])
# N = int(l[0])
# ll = []
# result = []
# results = ''
# if(N == 0):
#     print(0)
# else:
#     while N>=D:
#         ll.append(N%D)
#         N = int(N/D)
#     ll.append(N%D)
#     for i in range(len(ll)-1,-1,-1):
#         result.append(ll[i])
#         if results!='':
#             results = results+ ' ' +str(ll[i])
#         else:
#             results = results+str(ll[i])
#         # print(ll[i],end='')
# tag = 0
# for i in range(int(len(result)/2)):
#     if(result[i]!=ll[i]):
#         tag = -1
# if(tag==-1):
#     print('No')
# else:
#     print('Yes')
# print(results)

#A1027
l = input().split(' ')
D = 13
L = list(map(int,l))
ll = []
result = []
results = ''
for N in L:
    if(N == 0):
        print(0)
    else:
        while N>=D:
            ll.append(N%D)
            N = int(N/D)
        ll.append(N%D)
        for i in range(len(ll)-1,-1,-1):
            result.append(ll[i])
            # if results!='':
            #     results = results+ ' ' +str(ll[i])
            # else:
            #     results = results+str(ll[i])
            print(ll[i],end=' ')