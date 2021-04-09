#201812-1
# r,y,g = map(int,input().split())
# n = int(input())
# sum_t = 0  #记录小明上学总时间
# for i in range(n):
#     c,t = map(int,input().split())
#     if c == 0:
#         sum_t += t
#     elif c == 1:
#         sum_t += t
#     elif c == 2:
#         sum_t += (t+r)
#     else:
#         pass
# print(sum_t)

#201812-2
# def judge(r,g,y,t):
#     #返回当前处于哪个灯，剩余多少秒
#     if t<r:
#         return r-t
#     elif t>=r and t<r+g:
#         return 0
#     elif t>=r+g and t<r+g+y:
#         return r+g+y-t+r
#
# r,y,g = map(int,input().split())
# n = int(input())
# sum_t = 0  #记录小明放学总时间
# for i in range(n):
#     c,spend = map(int,input().split())
#     if c == 0:
#         sum_t += spend
#     elif c == 1:
#         temp = (r-spend + sum_t)%(r+g+y)
#         t = judge(r,g,y,temp)
#         sum_t += t
#     elif c == 2:
#         temp = (r+g+y-spend + sum_t)%(r+g+y)
#         t = judge(r,g,y,temp)
#         sum_t += t
#     elif c == 3:
#         temp = (r+g-spend + sum_t)%(r+g+y)
#         t = judge(r,g,y,temp)
#         sum_t += t
# print(sum_t)

#201809-1
# n = int(input())
# price = list(map(int,input().split()))
# new_price = [0 for i in range(n)]
# for i in range(n):
#     if i == 0:
#         new_price[i] = (price[i] + price[i+1])//2
#     elif i == n-1:
#         new_price[i] = (price[i - 1] + price[i]) // 2
#     else:
#         new_price[i] = (price[i - 1] + price[i + 1]+price[i]) // 3
# print(" ".join(map(str,new_price)))

#201809-2
# n = int(input())
# time = [0 for i in range(1000001)]
# for i in range(2*n):
#     start,end = map(int,input().split())
#     for j in range(start,end):
#         time[j] += 1
# print(time.count(2))

#201803-1
# l = list(map(int,input().split()))
# score = 0
# count = 0
# for i in range(len(l)):
#     if l[i] == 2:
#         count += 1
#         score += (count * 2)
#     else:
#         score += l[i]
#         count = 0
# print(score)

#201803-2
# n,L,t = map(int,input().split())
# location = list(map(int,input().split()))
# direction = [1 for i in range(n)]
# new_location = sorted(location)
# index = {}
# for i in range(n):
#     index[i] = location.index(new_location[i])
# for i in range(t):
#     for j in range(n):
#         new_location[j] += direction[j]
#         if new_location[j] == new_location[j-1]:
#             direction[j] = (-1)*direction[j]
#             direction[j-1] = (-1) * direction[j-1]
#         elif new_location[j] == 0 or new_location[j]==L:
#             direction[j] = (-1)*direction[j]
# index = sorted(index.items(),key=lambda x:x[1])
# for i in range(n):
#     if i == n-1:
#         print(new_location[index[i][0]])
#     else:
#         print(new_location[index[i][0]],end=' ')

