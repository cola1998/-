#201703-1
# n,k = map(int,input().split())
# l = list(map(int,input().split()))
# count = 0
# sum = 0
# for i in range(n):
#     sum += l[i]
#     if sum<k and i != n-1:
#         pass
#     else:
#         sum = 0
#         count += 1
# print(count)

#201703-2
# def yidong(l,x,n):
#     x_l = l.index(x)
#     if n > 0:
#         #向后移动
#         while(n!=0):
#             l[x_l] = l[x_l+1]
#             n -= 1
#             x_l += 1
#         l[x_l] = x
#     else:
#         #向前移动
#         while(n!=0):
#             l[x_l] = l[x_l - 1]
#             n += 1
#             x_l -= 1
#         l[x_l] = x
#     return l
#
# n = int(input())
# student = [i for i in range(1,n+1)]
# m = int(input())
# l = []
# for i in range(m):
#     l.append(list(map(int,input().split())))
# result = []
# for i in range(m):
#     student = yidong(student,l[i][0],l[i][1])
#
# for i in range(n):
#     if i == n-1:
#         print(student[i])
#     else:
#         print(student[i],end=' ')

#201703-4
