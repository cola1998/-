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

def clearExpiration(t):
    for i in range(1,len(ip_list)):
        ip_list[i].checkExpiration(t)

def getMinIP(t):
    expired_flag = -1
    for i in range(1, len(ip_list)):
        #ip_list[i].checkExpiration(t)
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


def setIP(ip, occupier, setT, t,status):  # ip：表示占用这个ip
    ip_list[ip].status = status
    ip_list[ip].occupier = occupier
    if setT == 0:
        ip_list[ip].expiration = t + tdef
        return t + tdef
    elif setT < t+tmin:
        ip_list[ip].expiration = t+tmin
        return t+tmin
    elif setT > t+tmax:
        ip_list[ip].expiration = t+tmax
        return t+tmax
    else:
        ip_list[ip].expiration = setT
        return setT


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
    if P[1] != '*' and P[1]!=h and P[2]!='REQ':
        continue
    if P[2] != 'DIS' and P[2] != 'REQ':
        continue
    if P[1] == '*' and P[2] != 'DIS':
        continue
    if P[1] == h and P[2] == 'DIS':
        continue
    if P[2] == 'DIS':
        # 检查发送主机的ip地址是否被占用
        r = checkIP(P[0])
        if r != -1:
            # 占用该ip地址
            tt = setIP(r, P[0], int(P[4]), t,0)
        else:
            r = getMinIP(t)
            if r != -1:
                tt = setIP(r, P[0], int(P[4]), t,0)
            else:
                continue  # 无多余地址 拒绝分配
        res.append([h, P[0], 'OFR', r, tt])
    elif P[2] == 'REQ':
        if P[1] != h:
            # bababab
            for j in range(1,len(ip_list)):
                if ip_list[j].occupier == P[0]:
                    if ip_list[j].status == 0:
                        ip_list[j].status = -1
                        ip_list[j].occupier = 0
                        ip_list[j].expiration = 0
        elif int(P[3]) <= N and ip_list[int(P[3])].occupier == P[0]:
            tt = setIP(int(P[3]), P[0], int(P[4]), t,1)
            res.append([h, P[0], 'ACK', int(P[3]), tt])
        else:
            res.append([h, P[0], 'NAK', int(P[3]), 0])
for i in range(len(res)):
    print(" ".join(map(str, res[i])))
