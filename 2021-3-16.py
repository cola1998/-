#201812-1  小明上学
# r,y,g = map(int,input().split())
# n = int(input())
# info = []
# time = 0
# for i in range(n):
#     tag, tt = map(int,input().split())
#     if tag == 0:
#         time += tt
#     elif tag == 1:
#         time += tt
#     elif tag == 2:
#         time += (tt+r)
#     elif tag == 3:
#         pass
# print(time)

#201812-2  小明放学
def judge(time,d,l):
    '''
    :param time: 到达该位置时间
    :param d: 出发时的灯
    :param l: 出发时剩余时间
    :return: now_d,r 当前灯，剩余时间
    '''
    xw =  [30,30,3]
    if d == 1: #刚出发时为红灯
        if time<l:
            return [1,l-time]
        elif time == l:
            return [3,0]
        else:
            if (time-l) < 30:#还处于绿灯
                return [3,0]
            else:
                time = time -l
                i = 1
                while time>0:
                    time -= xw[i]
                    i = i%3
                return [i+1,-1*time]
    elif d == 2:#刚出发时为黄灯
        if time <= l:
            return [2,l-time+30]
        else:
            time = time - l
            i = 0
            while time > 0:
                time -= xw[i]
                i = i % 3
            return [i + 1, -1 * time]
    elif d == 3:#刚出发时为绿灯
        if time < l:
            return [3,0]
        elif time == l:
            return [1,3+30]
        else:
            time = time - l
            i = 2
            while time > 0:
                time -= xw[i]
                i = i % 3
            return [i + 1, -1 * time]
# 自己思路  超时
# r,y,g = map(int,input().split())
# n = int(input())
# info = []
# time = 0 #从出发开始花费的时间
# for i in range(n):
#     tag, tt = map(int,input().split())
#     if tag == 0:
#         time += tt
#     else:
#         j, t = judge(time, tag, tt)
#         if j == 2:  # 黄灯
#             time += (t + 30)
#         else:
#             time += t
# print(time)

r,y,g = map(int,input().split())
n = int(input())
time = 0 #从出发开始花费的时间
for i in range(n):
    tag, tt = map(int,input().split())
    if tag == 0:
        time += tt
        continue
    elif tag == 1:
        tt += g
    elif tag == 2:
        tt += (r+g)
    tp = (tt - time) % (r+y+g)
    if tp>g:
        time += (tp-g)
print(time)

# r, y, g = map(int, input().split())
# n = eval(input())
# total = 0
# for _ in range(n):
#     m_type, m_time = map(int, input().split())
#     if m_type == 0:
#         total += m_time
#         continue
#     elif m_type == 1:
#         m_time += g
#     elif m_type == 2:
#         m_time += (r + g)
#     tem_time = (m_time-total) % (r + g + y)
#     if tem_time > g: #判断是否大于绿灯等待时间，大于那就需要再加；如果不，这时间点落在之前多加的绿灯区间，不管。
#         total += (tem_time - g)
# print(total)