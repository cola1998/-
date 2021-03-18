#201604-1  折点计数
# n = int(input())
# l = list(map(int,input().split()))
# count  = 0
# for i in range(1,n-1):
#     if l[i-1] < l[i] and l[i] > l[i+1]:
#         count += 1
#     elif l[i-1] > l[i] and l[i] < l[i+1]:
#         count += 1
# print(count)

#201604-2 俄罗斯方块  动态模拟执行
fgt = []#方格图
for i in range(15):
    fgt.append(list(map(int,input().split())))
xk = []#新加入的板块
for i in range(4):
    xk.append(list(map(int,input().split())))
x = int(input())  #表示最开始在哪一列

