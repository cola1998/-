# 201412-2 Z字形扫描
# n = int(input())
# info = []
# res = []
# for i in range(n):
#     info.append(list(map(int,input().split())))
# i = 0
# j = 0
# while True:
#     res.append(info[i][j])
#     if (i+j)%2==0:
#         pass
#     else:
#         if j>0 and i!=n-1:
#
#         elif i == n-1:
#         elif j == 0:
#             j += 1


# 201409-1 相邻数对
# n = int(input())
# l = list(map(int,input().split()))
# l = sorted(l)
# res = 0
# for i in range(1,n):
#     if l[i] - l[i-1] == 1:
#         res+= 1
# print(res)

# 201409-2 画图
# n = int(input())
# x = [[0 for i in range(100)] for j in range(100)]
#
# for i in range(n):
#     x1,y1,x2,y2 = map(int,input().split())
#     for j in range(y1,y2):
#         for z in range(x1,x2):
#             x[j][z] = 1
# res = 0
# for i in range(100):
#     #print(x[i])
#     res += x[i].count(1)
# print(res)

# 201409-3 字符串匹配
# pattern = input()
# tag = int(input()) #if tag == 0:表示大小写不敏感 tag==1 表示大小写敏感
# n = int(input())
# y_l = []
# if tag == 0:
#     pattern = pattern.lower()
#     for i in range(n):
#         y = input()
#         if pattern in y.lower():
#             print(y)
# elif tag == 1:
#     for i in range(n):
#         y = input()
#         if pattern in y:
#             print(y)
# leetcode
import copy
s = "abpcplea"
dictionary = ["a","b","c"]
res = ''
for i in range(len(dictionary)):
    temp_s = copy.copy(s)
    j = 0
    x = 0
    count = 0
    while j < len(s) and x < len(dictionary[i]):
        if s[j] != dictionary[i][x]:
            t = temp_s.index(s[j])
            temp_s = temp_s[:t] + temp_s[t+1:]
            j += 1
        else:
            count += 1 #匹配成功字母数+1
            j += 1
            x += 1
    if count == len(dictionary[i]): #匹配成功
        if len(res) < len(dictionary[i]):
            res = dictionary[i]
        elif len(res) == len(dictionary[i]) and res>dictionary[i]:
            res = dictionary[i]  #长度相等，但字典序更小
print(res if res != '' else None)