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

# 大模拟
# 202104-3 DHCP服务器
class IP:
    def __init__(self, address, status, occupier, expiration):
        self.address = address  # ip地址 1-N
        self.status = status  # 状态 -1-未分配 0-待分配 1-占用 2-过期
        self.occupier = occupier  # 当状态是-1时 无占用者  其他状态均有一名占有者
        self.expiration = expiration  # 过期时间 未分配和过期状态 -1和2

    def deallocate(self):  # 取消分配
        self.status = -1
        self.occupier = 0
        self.expiration = 0

    def checkExpiration(self, t):  # 检查是否过期  t 是传入的当前时间，用于判断
        if self.expiration <= t:
            if self.status == 0:
                self.status = -1
                self.occupier = 0
                self.expiration = 0
            else:
                self.status = 2
                self.expiration = 0
            return True
        else:
            return False


def getMinIP():
    expired_flag = 0
    for i in range(1, len(ip_list)):
        if ip_list[i].status == -1:
            return i
        else:
            if ip_list[i].checkExpiration(t) == True:
                expired_flag = i
    if expired_flag != -1:
        return expired_flag
    else:
        return -1 # 获取失败 已经全部分配好了


def checkIP(sender):  # 检查是否给发送者分配过ip
    for i in range(1, len(ip_list)):
        if ip_list[i].occupier == sender and ip_list[i].checkExpiration(t) == False:
            return i
    return -1


def setIP(ip, occupier, setT, t):  # ip：表示占用这个ip
    ip_list[ip].status = 1
    ip_list[ip].occupier = occupier
    if setT == 0:
        ip_list[ip].expiration = t + tdef
        return t + tdef
    elif setT < tmin:
        ip_list[ip].expiration = t + tmin
        return t + tmin
    elif setT > tmax:
        ip_list[ip].expiration = t + tmax
        return t + tmax
    else:
        ip_list[ip].expiration = t + setT
        return t + setT


[N, tdef, tmax, tmin, h] = input().split()  # h是主机！
N = int(N)
tdef = int(tdef)
tmax = int(tmax)
tmin = int(tmin)
n = int(input())  # 表示收到的报文数
ip_list = [IP(i, -1, 0, 0) for i in range(N + 1)]  # 初始化ip池
res = []
for i in range(n):
    P = input().split()  # 收到的报文
    t = int(P[0])  # 当前时间
    P.pop(0)  # P[0]发送主机 P[1]接受主机 P[2]报文类型 P[3]IP地址 P[4]过期时间

    if P[2] != 'DIS' and P[2] != 'REQ':
        continue
    if P[1] == '*' and P[2] != 'DIS':
        continue
    if P[1] == h and P[2] != 'DIS':
        continue
    if P[2] == 'DIS':
        # 检查发送主机的ip地址是否被占用
        r = checkIP(P[0])
        if r != -1:
            # 占用该ip地址
            tt = setIP(r, P[0], int(P[4]), t)
        else:
            r = getMinIP()
            if r != -1:
                tt = setIP(r, P[0], int(P[4]), t)
            else:
                continue  # 无多余地址 拒绝分配
        res.append([h, P[0], 'OFE', r, tt])
    elif P[2] == 'REQ':
        if P[1] != h:
            # bababab
            for i in range(1,len(ip_list)):
                if ip_list[i].occupier == P[0]:
                    if ip_list[i].status == 0:
                        ip_list[i].status = -1
                        ip_list[i].occupier = 0
                        ip_list[i].expiration = 0
        elif int(P[3]) <= N and ip_list[int(P[3])].occupier == P[0]:
            tt = setIP(int(P[3]),P[0],int(P[4]),t)
            res.append([h, P[0], 'ACK',P[3], tt])
        else:
            res.append([h,P[0],'NAK',P[3],0])
for i in range(len(res)):
    print(" ".join(map(str, res[i])))
