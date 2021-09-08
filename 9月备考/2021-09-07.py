# 201909-1  小明种苹果
# n, m = map(int, input().split())
# info = [0 for i in range(n)]
# k_l = []
# for i in range(n):
#     al = list(map(int, input().split()))
#     info[i] = al[0]
#     count = 0  # 记录该苹果树疏果个数
#     for j in range(1, len(al)):
#         if al[j] < 0:
#             count += abs(al[j])
#         else:
#             pass
#     k_l.append(count)
#     info[i] -= count
# print(sum(info), k_l.index(max(k_l)) + 1, max(k_l))


# 201909-2 小明种苹果(续)
# n = int(input())  # n棵树
# e = 0  # 代表连续三棵树发生苹果掉落情况的组数
# tag_l = [0 for i in range(n)]  # 1代表该树发生掉落了，0表示没发生掉落
# info = [0 for i in range(n)]  # 记录每棵树当前数量
# for i in range(n):
#     al = list(map(int, input().split()))
#     al.pop(0)
#     info[i] = al[0]
#     for j in range(1, len(al)):
#         if al[j] > 0:
#             # 表示重新整理了数据
#             if al[j] != info[i]:  # 代表有果子掉落
#                 info[i] = al[j]
#                 tag_l[i] = 1
#         else:  # al[j]<=0
#             # 表示进行了疏果操作
#             info[i] -= abs(al[j])
# print(info)
# # 统计组数
# for i in range(n):
#     if i == 0:
#         if tag_l[i] == 1 and tag_l[i + 1] == 1 and tag_l[n - 1] == 1:
#             e += 1
#     elif i == n - 1:
#         if tag_l[n - 1] == 1 and tag_l[0] == 1 and tag_l[i - 1] == 1:
#             e += 1
#     elif tag_l[i] == 1 and tag_l[i + 1] == 1 and tag_l[i - 1] == 1:
#         e += 1
# print(sum(info), sum(tag_l), e)

# 201903-1  小中大
# n = int(input())
# l = list(map(int, input().split()))
# res = [max(l),min(l)]
# #求中位数
# if n % 2 != 0:
#     res.append(l[n//2])
# else:
#     mid_n = round((l[n//2-1] + l[n//2])/2,1)
#     if str(mid_n)[-1] == '0':
#         res.append(round(mid_n))
#     else:
#         res.append(mid_n)
# res = sorted(res,reverse=True)
# print(" ".join(map(str,res)))

# 201903-2 二十四点
# 简便算法....
# n = int(input())
# for i in range(n):
#     res = eval(input().replace('x','*').replace('/','//'))
#     if res == 24:
#         print('Yes')
#     else:
#         print('No')

# 认真算 算了
# n = int(input())
# info = []
# y = [0,0,1,1]  #代表 + - * / 运算符号的优先级
# for i in range(n):
#     al = list(input().split())
#     s_stack = []  # 模拟数据栈
#     f_stack = []  # 模拟符号栈
#     for j in range(len(al)):
#         if al[j] <='9' and al[j]>='0':
#             s_stack.append(int(al[j]))
#         else:
#             if al[j] == '+' or al[j] == '-':
#                 f_stack.append(al[j])

