#例题1 勇者斗恶龙
# while True:
#     n,m = map(int,input().split())
#     if n==0 and m == 0:
#         break
#     else:
#         head = []
#         for i in range(n):
#             head.append(int(input()))
#         head = sorted(head)
#         hero = []
#         for i in range(m):
#             hero.append(int(input()))
#         hero = sorted(hero)
#         cost = 0  #记录花费
#         cur = 0  #记录处理到第几个头了
#         for i in range(m):
#             if head[cur] <= hero[i]:
#                 cost += hero[i]
#                 cur += 1
#             if cur == n:
#                 break
#         if cur == n:
#             print(cost)
#         else:
#             print('Loowater is doomed!')
'''
输入
2 3
5
4
7
8
4
2 1
5 
5
10
0 0
'''

#例题2
# while True:
#     n = int(input())
#     count = 0
#     if n == 0:
#         break
#     else:
#         count += 1
#         l = []
#         for i in range(n):
#             l.append(list(map(int,input().split())))
#         l = sorted(l,key=lambda x:x[1],reverse=True)
#         late = 0 #记录最晚结束时间
#         start = 0
#         for i in range(len(l)):
#             start += l[i][0]
#             if start+l[i][1]>late:
#                 late = start+l[i][1]
#         print("Case {0}: {1}".format(count,late))
'''
输入：
3
2 5
3 2
2 1
3
3 3
4 4
5 5
0
'''
#例题3  分金币问题
n = int(input())
total = 0
l = []
for i in range(n):
    x = int(input())
    total += x
    l.append(x)
M = int(total/n)
C = [0 for i in range(n)]#??
for i in range(n):#递推C数组
    C[i] = C[i-1] + l[i] - M



#例题4 ??数学原理还有待研究
# import math
# n,m = map(int,input().split())
# ans = 0
# for i in range(n):
#     pos = (i/n)*(n+m)
#     ans += abs(pos-math.floor(pos+0.5))/(n+m)
# print(round(ans*10000,4))