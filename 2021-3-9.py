#201609-1
# n = int(input())
# l = list(map(int,input().split()))
# max = 0
# for i in range(1,n):
#     if abs(l[i] - l[i-1])>max:
#         max = abs(l[i] - l[i-1])
# print(max)

#201609-2
'''
测试样例
21
4 5 5 3 5 5 3 5 5 5 5 5 5 5 5 5 5 5 5 5 3
'''
# n = int(input())
# l = list(map(int,input().split()))
# site = [[i*0 for i in range(5)] for row in range(20)]
# # i*5+j+1
# seat = [5 for i in range(20)]  #存储每排可容纳人数
# result = []
#
# for i in range(n):
#     p = -1
#     for s in range(len(seat)):
#         if seat[s] >= l[i]:
#             p = s
#             break
#     if p == -1:
#         #查找空余座位分配
#         if sum(seat)<l[i]:
#             pass
#         else:
#             r = []
#             k = l[i]
#             for ii in range(20):
#                 if k == 0:
#                     break
#                 if seat[ii] == 0:
#                     continue
#                 for jj in range(5):
#                     if site[ii][jj] == 0:
#                         r.append(ii*5+jj+1)
#                         k -= 1
#                         seat[ii] -= 1
#                     if k == 0:
#                         result.append(r)
#                         break
#     else:
#         k = l[i] #待分配座位数
#         seat[p] -= k
#         r = []
#         for j in range(5):
#             if site[p][j] == 0:
#                 site[p][j] = 1
#                 k -= 1
#                 r.append(p*5+j+1)
#             if k == 0:
#                 result.append(r)
#                 break
# for i in result:
#     for j in i:
#         print(j,end=' ')
#     print()

#201609-3炉石传说
