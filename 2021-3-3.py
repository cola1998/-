#201409-03
# s = input()
# tag = input()
# n = int(input())
# if tag=='0':
#     s = s.lower()
#     for i in range(n):
#         x = input()
#         temp = x.lower()
#         if s in temp:
#             print(x)
# else:
#     for i in range(n):
#         x = input()
#         if s in x:
#             print(x)
#201409-4
#无向图多源点最短路径问题 可使用bfs求解
n,m,k,d = map(int,input().split())
branch = []
for i in range(m):
    branch.append(input().split())
clients = []
for i in range(k):
    clients.append(input().split())
no_list = []
for i in range(d):
    no_list.append(input().split())

#201412-1 门禁系统
# n = int(input())
# l = input().split()
# result = []
# d = {}
# for i in l:
#     if i in d.keys():
#         d[i] += 1
#         print(d[i],end='')
#     else:
#         d[i] = 1
#         print(1,end='')
#     if i == len(l)-1:
#         print()
#     else:
#         print('',end=' ')

#201412-2
#z字形扫描 观察到规律是先扫描下标和为2，3,4,5,6...的顺序
# 和为奇数是按照升序排列 和为偶数是按照降序排列
# n = int(input())
# l = []
# for i in range(n):
#     l.append(list(map(int,input().split())))
# i=0
# j=0
# while i<n and j<n:
#     print(l[i][j], end='')
#     if i == n-1 and j == n-1:
#         print('')
#     else:
#         print('',end=' ')
#     if (i + j) % 2 == 0:
#         if i > 0 and j != n-1:
#             i = i - 1
#             j = j + 1
#         elif j == n-1:
#             i += 1
#         else:
#             j += 1
#     else:
#         if j > 0 and i != n-1:
#             j = j - 1
#             i = i + 1
#         elif i == n-1:
#             j += 1
#         else:
#             i += 1

#201412-3集合竞价 没看懂题目
# record = []
# # for s in sys.stdin:
# #     record.append(list(s.split()))
# while True:
#     x = input()
#     if x == "":
#         break
#     record.append(x.split())
# for i in range(len(record)):
#     if record[i][0] == 'buy':