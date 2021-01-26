# 3.6字符串处理
# codeup 5901 回文串
# l = input()
# tag = 0
# for i in range(int(len(l)/2)):
#     if(l[i]!=l[len(l)-1-i]):
#         tag = -1
#         break
# if(tag==-1):
#     print('NO')
# else:
#     print('YES')
# B1009
# 注意是单词顺序调换
# l = input().split(' ')
# result = ''
# for i in range(len(l)-1,-1,-1):
#     if result=='':
#         result = result+l[i]
#     else:
#         result = result+' '+l[i]
# print(result)

# B1006
# S = ['B','S']
# l = int(input())
# result = []
# results = ''
# if(l>=100):
#     results=results+int(l / 100)*'B'
#     results=results+int((l % 100)/10)*'S'
#     for i in range(1,l%10+1):
#         results = results + str(i)
#     print(results)
# elif 100>l>=10:
#     results = results + int(l/10) * 'S'
#     for i in range(1, l % 10 + 1):
#         results = results + str(i)
#     print(results)
# else:
#     for i in range(1, l + 1):
#         results = results + str(i)
#     print(results)

# B1021
from collections import defaultdict

x = input()
result = defaultdict(list)
for i in range(len(x)):
    result[int(x[i])].append(1)
key = []
for i in result.keys():
    key.append(i)
key.sort()
for i in range(len(key)):
    print("{0}:{1}".format(key[i], len(result[key[i]])))
