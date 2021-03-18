#201509-1
# n = int(input())
# l = list(map(int,input().split()))
# count = 0
# for i in range(1,n):
#     if l[i] != l[i-1]:
#         count += 1
# print(count+1)

# 201509-2
# def isRun(year):
#     if year % 400 == 0:
#         return 1
#     elif year % 4 == 0 and year % 100 != 0:
#         return 1
#     else:
#         return 0
#
#
# y = int(input())
# d = int(input())
# days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# # 计算d是y年的几月几日
# days[1] += isRun(y)
# i = 0
# while d > 0:
#     d -= days[i]
#     i += 1
# if d <= 0:
#     i -= 1
#     d += days[i]
# print(i+1)
# print(d)

#201509-3
import re
def trans(matches):
    var = matches.group('var')
    if var in d:
        return d[var]
    else:
        return ""

m,n = map(int,input().split())
l = []
d = {}
for i in range(m):
    l.append(input())
for i in range(n):
    l2 = input().rstrip("\"").split(" \"")
    d[l2[0]] = l2[1]

for i in range(len(l)):
    print(re.sub(r'{{ (?P<var>\w*) }}',trans,l[i]))

#re.sub()函数实现正则的替换
#用法稍微有点复杂
'''
re.sub(pattern, repl, string, count=0, flags=0)
pattern 模式字符串
repl 被替换的 可以是字符串，也可以是函数
string 
(?P<name>...) 给group命名了，
'''
#输入
# 11 2
# <!DOCTYPE html>
# <html>
# <head>
# <title>User {{ name }}</title>
# </head>
# <body>
# <h1>{{ name }}</h1>
# <p>Email: <a href="mailto:{{ email }}">{{ email }}</a></p>
# <p>Address: {{ address }}</p>
# </body>
# </html>
# name "David Beckham"
# email "david@beckham.com"
