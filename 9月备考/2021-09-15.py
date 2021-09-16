# 201403-2  窗口
# n, m = map(int, input().split())
# c_l = []
# priority = [i for i in range(n, 0, -1)]  # 优先级从1到n
# for i in range(n):
#     c_l.append(list(map(int, input().split())))
# d_l = []
# # 判断每次点击的位置属于哪个窗口 然后输出最顶层的序号
# for i in range(m):
#     x, y = map(int, input().split())
#     res = -1  # 记录选择窗口标号
#     minp = n + 1  # 记录最小的优先级
#     for j in range(n):
#         if x >= c_l[j][0] and x <= c_l[j][2] and y >= c_l[j][1] and y <= c_l[j][3]:
#             if priority[j] < minp:
#                 minp = priority[j]
#                 res = j
#     if res != -1:
#         print(res + 1)
#         for i in range(n):
#             if priority[i] < minp:
#                 priority[i] += 1
#         priority[res] = 1
#     else:
#         print("IGNORED")

#201312-2 ISBN号码  9位数字 1位识别码 3位分隔符
rows = input()
s = rows.replace('-','')
res = 0
for i in range(len(s)-1):
    res += int(s[i])*(i+1)
x = res % 11
if x == 10 and s[-1]=='X':
    print('Right')

elif s[-1] != 'X' and x == int(s[-1]):
    print("Right")
else:
    if x != 10:
        rows = rows[:-1]+str(x)
        print(rows)
    else:
        rows = rows[:-1] + 'X'
        print(rows)