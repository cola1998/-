#201803-1
#process = list(map(int,input().split()))
# score = 0
# count = 1  #暂存连跳次数
# for i in range(len(process)):
#     if process[i] == 1:
#         score += 1
#         count = 1
#     elif process[i] == 2:
#         score += 2 * count
#         count += 1
#     else:
#         print(score)
#         break

#约束传播比较重要

#201803-2
# n,L,t = map(int,input().split())
# l_old = list(map(int,input().split()))
# l = sorted(l_old)
# d = {}
# for i in range(n):
#     d[i] = l.index(l_old[i])
# direction = [1 for i in range(n)]
#
# for i in range(t):
#     for j in range(n):
#         l[j] = l[j]+direction[j]
#         #两个球位置相同 或者 到达边界 direction变为原来的相反数
#         if l[j] == 0 or l[j] == L:
#             direction[j] = -1*direction[j]
#         elif l[j] == l[j-1]:#只有相邻小球有碰撞机会
#             direction[j] = -1 * direction[j]
#             direction[j-1] = -1 * direction[j-1]
# for i in range(n):
#     if i != n-1:
#         print(l[d[i]],end=' ')
#     else:
#         print(l[d[i]])

#201803-3
import re
n,m  = map(int,input().split())
rule = []
for i in range(n):
    rule.append(input())
q = []
for i in range(m):
    q.append(input())
    