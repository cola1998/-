# 201912-1
# n = int(input())
# count = 0  #记录现在报数到哪里
# l = [0,0,0,0]
# i = 0  #标记到哪个人了
# while n != 0:
#     count += 1
#     if count%7==0 or '7' in str(count):
#         l[i] += 1
#     else:
#         n -= 1
#     i = (i+1)%4
# for i in range(0,len(l)):
#     print(l[i])

# 201912-2
# n = int(input())
# info = []
# x_0 = [0,0,1,-1]
# y_0 = [1,-1,0,0]
# x_1 = [1,1,-1,-1]
# y_1 = [-1,1,-1,1]
# for i in range(n):
#     info.append(list(map(int,input().split())))
# scores = [0,0,0,0,0]
# count = 0
# for i in range(n):
#     x,y = info[i]
#     tag = 0
#     for j in range(4):
#         if [x+x_0[j],y+y_0[j]] not in info:
#             tag = 1
#     if tag == 0:
#         count += 1
#         score = 0
#         for j in range(4):
#             if [x+x_1[j],y+y_1[j]] in info:
#                 score += 1
#         scores[score] += 1
# for i in scores:
#     print(i)

# 201909-1
# n,m = map(int,input().split())
# info = []
# sum_t = 0
# k = 0
# max = 0
# for i in range(n):
#     l = list(map(int,input().split()))
#     count = 0
#     for j in range(1,len(l)):
#         count += abs(l[j])
#     if count > max:
#         k = i
#         max = count
#     sum_t += (l[0]-count)
# print("{0} {1} {2}".format(sum_t,k+1,max))

# 201909-2
# n = int(input())
# info = []
# sum_t = 0
# count = 0 #d
# tag_l = [0 for i in range(n)]
# for i in range(n):
#     l = list(map(int,input().split()))
#     m = l[1]
#     tag = 0
#     for j in range(2,len(l)):
#         if l[j] <= 0:
#             m -= abs(l[j])
#         else:
#             if m != l[j]:
#                 tag = 1
#                 tag_l[i] = 1
#                 m = l[j]
#     if tag == 1:
#         count += 1
#     sum_t += m
# sum_e = 0
# for i in range(n):
#     if i == 0 and tag_l[i] == 1 and tag_l[n-1] == 1 and tag_l[i+1]==1:
#         sum_e += 1
#     elif i == n-1 and tag_l[i] == 1 and tag_l[i-1] == 1 and tag_l[0]==1:
#         sum_e += 1
#     elif tag_l[i] == 1 and tag_l[i-1] == 1 and tag_l[i+1]==1:
#         sum_e += 1
#
# print("{0} {1} {2}".format(sum_t,count,sum_e))

# 201903-1
# n = int(input())
# l = list(map(int, input().split()))
# ans = [max(l), min(l)]
# if n % 2 == 0:
#     x = (l[int(n / 2) - 1] + l[int(n / 2)]) / 2
#     if str(x)[-2:] == '.0':
#         ans.append(int(x))
#     else:
#         ans.append(round(x, 1))
# else:
#     ans.append(l[int(n / 2)])
# ans = sorted(ans, reverse=True)
# print(" ".join(map(str, ans)))

#201903-2
n = int(input())
for i in range(n):
    x = input().replace('/','//').replace('x','*')
    print('Yes' if eval(x)==24 else "No")