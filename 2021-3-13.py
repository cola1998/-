#201712-1
# n = int(input())
# l = list(map(int,input().split()))
# l = sorted(l)
# min = 99999
# for i in range(n):
#     if abs(l[i] - l[i-1])<min:
#         min = abs(l[i]-l[i-1])
# print(min)

#201712-2
# n,k = map(int,input().split())
# count = 0
# status = [1 for i in range(n)]  #1表示还存活在游戏中
# while sum(status) != 1:
#     for i in range(n):
#         if status[i]!=0:
#             count += 1  #记录报数
#             if count%k==0 or str(count)[-1] == str(k):
#                 status[i] = 0
#                 if sum(status) == 1: #判断可以退出了就及时退出 不要等到下次循环
#                     break
# print(status.index(1)+1)

#201712-3
[n,s,t] = input().split()
crontab = []
n = int(n)
#系统开始时间处理

for i in range(n):
    crontab.append(input())
print(n,s,t)