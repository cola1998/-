# 201509-1 数列分段
# n = int(input())
# l = list(map(int,input().split()))
# res = 0
# for i in range(1,n):
#     if l[i] != l[i-1]:
#         res += 1
# res += 1
# print(res)


# 201312-1 出现次数最多的数
# n = int(input())
# l = list(map(int,input().split()))
# s = list(set(l))
# min_c = 0
# max_c = 0
# for i in range(len(s)):
#     c = l.count(s[i])
#     if c > max_c:
#         max_c = c
#         min_c = s[i]
#     elif c == max_c and min_c>s[i]:
#         min_c = s[i]
#     else:
#         pass
# print(min_c)

# 201503-1 图像旋转
# n,m = map(int,input().split())
# info = []
# newT = []
# for i in range(n):
#     l = list(map(int,input().split()))
#     info.append(l)
# for j in range(m-1,-1, -1):
#     l = []
#     for i in range(n):
#         l.append(info[i][j])
#     newT.append(l)
# for i in range(m):
#     print(" ".join(map(str,newT[i])))

# 201503-2 数字排序
# n = int(input())
# l = list(map(int,input().split()))
# res = {}
# s = list(set(l))
# for i in range(len(s)):
#     res[s[i]] = l.count(s[i])
# res = sorted(res.items(),key=lambda x:(x[1],-x[0]),reverse=True)
# for i in range(len(res)):
#     print("{0} {1}".format(res[i][0],res[i][1]))

# 201509-2 日期计算
# y = int(input())
# d = int(input())
# days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]
# res = []  # 月份和日期
# # 先判断年份是否是闰年
# if y % 4 == 0 and y % 100 != 0:
#     days[1] += 1
# elif y % 400 == 0:
#     days[1] += 1
# else:
#     pass
# i = 0
# while d != 0:
#     if d > days[i]:
#         d -= days[i]
#     else:
#         break
#     i += 1
# print(i+1)
# print(d)
