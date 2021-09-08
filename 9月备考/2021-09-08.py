# 201812-1 小明上学
# r, y, g = map(int, input().split())
# n = int(input())
# total_t = 0 # 表示主进程的时间
# for i in range(n):
#     tag, t = map(int,input().split())
#     if tag == 0: #表示经过一段路
#         total_t += t
#     elif tag == 1: #表示现在的灯是红灯
#         total_t += t
#     elif tag == 2: #表示现在是黄灯
#         total_t += (t+r)
#     else:
#         pass
# print(total_t)

# 201812-2 小明放学
# r, y, g = map(int, input().split())
# n = int(input())
# total_t = 0 # 表示主进程的时间
# l = [i for i in range(r,0,-1)]
# l += [i*0 for i in range(g)]
# l += [i+r for i in range(y,0,-1)]
# num = r+g+y
# for i in range(n):
#     tag,t = map(int,input().split())
#     if tag == 0:
#         total_t += t
#     elif tag == 1:  #表示刚出发时是红灯 判断现在是什么颜色的灯
#         temp_t = (r-t+total_t)%(num)
#         total_t += l[temp_t]
#     elif tag == 2: # 表示刚出发时是黄灯 判断现在剩余需要等待时间
#         temp_t = (r + g + y-t + total_t) % (num)
#         total_t += l[temp_t]
#     elif tag == 3:
#         temp_t = (r + g -t+total_t)%num
#         total_t += l[temp_t]
# print(total_t)

#201809-1 卖菜
# import math
# n = int(input())
# price = list(map(int,input().split()))
# res = []
# for i in range(n):
#     if i == 0:
#         temp_price = math.floor((price[i] + price[i+1])/2)
#     elif i == n-1:
#         temp_price = math.floor((price[i] + price[i-1])/2)
#     else:
#         temp_price = math.floor((price[i-1]+price[i]+price[i+1])/3)
#     res.append(temp_price)
# print(" ".join(map(str,res)))

#201809-2 买菜
n = int(input())
tt = []
h_t = []
max_h = 0
for i in range(n):
    a,b = map(int,input().split())
    h_t.append([a,b])
    max_h = max(max_h,b)
w_t = []
max_w = 0
for i in range(n):
    a,b = map(int,input().split())
    w_t.append([a,b])
    max_w = max(max_w,b)
tt = [0 for i in range(max(max_h,max_w)+1)]
for i in range(n):
    for j in range(h_t[i][0]+1,h_t[i][1]+1):
        tt[j] += 1
    for j in range(w_t[i][0]+1,w_t[i][1]+1):
        tt[j] += 1
print(tt.count(2))