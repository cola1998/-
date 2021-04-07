#202012-1
# n = int(input())
# sum_s = 0
# for i in range(n):
#     w,score = map(int,input().split())
#     sum_s += (w*score)
# if sum_s < 0:
#     print(0)
# else:
#     print(sum_s)

#202212-2  ??为什么会超时
# m = int(input())
# info = {}
# keys = []
# for i in range(m):
#     y,result = map(int,input().split())
#     if y not in keys:
#         keys.append(y)
#         info[y] = [0,0]
#     if result == 0:
#         info[y][0] += 1
#     else:
#         info[y][1] += 1
# keys = sorted(keys)
# #正反遍历两次求解  前缀和
# info_0 = []
# count = 0
# for i in range(len(keys)):
#     count += info[keys[i-1]][0]
#     info_0.append(count)
#
# #反向遍历
# info_1 = []
# count = 0
# for j in range(len(keys)-1,-1,-1):
#     count += info[keys[j]][1]
#     info_1.append(count)
# info_1 = info_1[::-1]
#
# max = 0
# k = -1
# for i in range(len(keys)):
#     count = info_0[i]+info_1[i]
#     if count >= max:
#         max = count
#         k = i
# print(keys[k])

#202009-1
# n,X,Y = map(int,input().split())
# l = {}
# for i in range(n):
#     x,y = map(int,input().split())
#     d = pow((X-x),2) + pow((Y-y),2)
#     l[i] = d
# l = sorted(l.items(),key=lambda x:x[1])
# for i in range(3):
#     print(l[i][0]+1)

#202009-2
# n,k,t,xl,yd,xr,yu = map(int,input().split())
# info = []
# total = 0
# total_j = 0
# for i in range(n):
#     count = 0
#     l = list(map(int,input().split()))
#     tag = 0
#     for j in range(0,len(l),2):
#         if l[j]>=xl and l[j]<=xr and  l[j+1]>=yd and l[j+1]<=yu:
#             count += 1
#             tag = 1
#             if count >= k:
#                 total += 1
#                 break
#         else:
#             count = 0
#     if tag == 1:
#         total_j += 1
# print(total_j)
# print(total)

#202003-1
# n,m = map(int,input().split())
# info_a = []
# info_b = []
# for i in range(n):
#     t = input().split()
#     if t[2] == 'A':
#         info_a.append([int(t[0]),int(t[1])])
#     else:
#         info_b.append([int(t[0]), int(t[1])])
# query = []
# for i in range(m):
#     a,b,c = map(int,input().split())
#     list_1 = []
#     list_2 = []
#     for x,y in info_a:
#         if a+b*x+c*y >= 0:
#             list_1.append([x,y])
#         else:
#             list_2.append([x,y])
#
#     if len(list_1) == len(info_a) and len(list_2) == 0: # 至少能够把a类点分出来 将其存放在list_1中
#         list_1 = []
#         for x, y in info_b: # 检查b类点是否能够分出来
#             if a+b*x+c*y >= 0:
#                 list_1.append([x,y])
#             else:
#                 list_2.append([x,y])
#         if len(list_2) == len(info_a) and len(list_1) == 0:
#             print('Yes')
#         else:
#             print('No')
#     elif len(list_2) == len(info_a) and len(list_1) == 0:
#         list_2 = []
#         for x, y in info_b:  # 检查b类点是否能够分出来
#             if a + b * x + c * y >= 0:
#                 list_1.append([x, y])
#             else:
#                 list_2.append([x, y])
#         if len(list_1) == len(info_b) and len(list_2) == 0:
#             print('Yes')
#         else:
#             print('No')
#     else:#a类点都无法分出
#         print('No')

# n,m = map(int,input().split())
# info = []
# for i in range(n):
#     t = input().split()
#     info.append([int(t[0]), int(t[1]),t[2]])
# query = []
# for i in range(m):
#     a,b,c = map(int,input().split())
#     tag_gt = -1
#     tag_lt = -1
#     tag = -1
#     for j in range(len(info)):
#         if a + b*info[j][0] + c*info[j][1] >= 0:
#             if tag_gt == -1:
#                 tag_gt = info[j][2]
#                 tag_lt = 'B' if tag_gt=='A' else 'A'
#             if tag_gt != info[j][2]:
#                 print('No')
#                 tag = 0
#                 break
#         else:
#             if tag_lt == -1:
#                 tag_lt = info[j][2]
#                 tag_gt = 'A' if tag_lt == 'B' else 'B'
#             if tag_lt != info[j][2]:
#                 print('No')
#                 tag = 0
#                 break
#     if tag == -1:
#         print('Yes')


#202003-2
# n,a,b = map(int,input().split())
# u = {}
# v = {}
# for i in range(a):
#     index,value = map(int,input().split())
#     u[index] = value
# for i in range(b):
#     index, value = map(int, input().split())
#     v[index] = value
# ans = 0
# for key in u.keys():
#     if key in v:
#         ans += u[key]*v[key]
# print(ans)

#202012-3
