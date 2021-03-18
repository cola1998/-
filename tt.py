# # 权限查询  #201612-3   100分
# pris = {}  # privileges
# roles = {}
# users = {}
# # 权限
# p = int(input())
# for i in range(p):
#     s = input().split(":")
#     pris[s[0]] = s[1] if len(s) == 2 else ""  # 因为保证合法性所以其实不用写这段
#
# # 角色
# r = int(input())
# for i in range(r):
#     s = input().split()
#     n = int(s[1])  # 角色权限个数
#     mypri = []
#     for j in range(2, 2 + n):
#         mypri.append(s[j].split(":"))
#     roles[s[0]] = mypri  # 以列表储存
#
# # 用户
# u = int(input())
# for i in range(u):
#     s = input().split()
#     n = int(s[1])  # 用户角色个数
#     myrole = []
#     for j in range(2, 2 + n):
#         myrole.append(s[j])
#     mypri = {}
#     for role in myrole:  # 遍历用户
#         for pri in roles[role]:  # 遍历每个用户权限
#             if (len(pri) == 1):  # 无等级权限
#                 mypri[pri[0]] = ""
#             elif (pri[0] not in mypri):  # 等级权限首次存储
#                 mypri[pri[0]] = int(pri[1])
#             else:  # 比较存入权限最大等级
#                 mypri[pri[0]] = max(mypri[pri[0]], int(pri[1]))
#     users[s[0]] = mypri  # 用字典存储
#
# # 查询
# q = int(input())
# for i in range(q):
#     name, this_pri = input().split()  # 用户名，权限
#     this_pri = this_pri.split(":")  # 区分是否有等级
#
#     if (name in users):  # 用户存在
#         if (this_pri[0] in users[name]):  # 权限名存在
#             if (len(this_pri) == 1):
#                 if (users[name][this_pri[0]] == ""):  # 无等级权限
#                     print("true")
#                 else:
#                     print(users[name][this_pri[0]])  # 查询等级
#             elif (len(this_pri) == 2):  # 带等级
#                 if (users[name][this_pri[0]] == ""):  # 无效查询
#                     print("false")
#                 elif (int(this_pri[1]) <= users[name][this_pri[0]]):  # 等级满足
#                     print("true")
#                 else:  # 等级不满足
#                     print("false")
#         else:
#             print("false")
#     else:
#         print("false")

N, K = map(int, input().split())
Keys = list(range(1, N + 1))
time_table = []#钥匙存取的时间记录
for i in range(K):
    w, s, c = map(int, input().split())
    time_table.append((s, True, w))#时间点，是否为取出钥匙， 钥匙编号
    time_table.append((s + c, False, w))
time_table.sort()#按照时间点是否取出钥匙，钥匙编号排序
print(time_table)
for time, take, key_number in time_table:
    if take:#取钥匙
        Keys[Keys.index(key_number)] = 0#0代表钥匙被取出
    else:
        Keys[Keys.index(0)] = key_number#从左边开始找空位还钥匙
print(" ".join(map(str, Keys)))