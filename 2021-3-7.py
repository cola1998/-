#201512-1
# n = input()
# sum = 0
# for i in range(len(n)):
#     sum += int(n[i])
# print(sum)

#201512-2
# n,m = map(int,input().split())
# l = []
# d = [[int(i/i) for i in range(1,m+1)] for row in range(n)]
# for i in range(n):
#     l.append(list(map(int,input().split())))
#
# #横向扫描
# for i in range(n):
#     for j in range(1,m-1):
#         if l[i][j-1] == l[i][j] and l[i][j] == l[i][j+1]:
#             d[i][j] = 0
#             d[i][j-1] = 0
#             d[i][j+1] = 0
# #纵向扫描
# for i in range(m):
#     for j in range(1,n-1):
#         if l[j-1][i] == l[j][i] and l[j+1][i] == l[j][i]:
#             d[j][i] = 0
#             d[j-1][i] = 0
#             d[j+1][i] = 0
# for i in range(n):
#     for j in range(m):
#         print((d[i][j] and l[i][j]),end='')
#         if j != m-1:
#             print('',end=' ')
#         else:
#             print('')

#201512-3
# m,n,q = map(int,input().split())
# l = []
# for i in range(q):
#     l.append(list(input().split()))

#201512-4
n,m = map(int,input().split())
l = []
for i in range(m):
    l.append(map(int,input().split()))