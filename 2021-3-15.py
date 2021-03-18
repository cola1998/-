# 201809-1  卖菜
# n = int(input())
# price = list(map(int, input().split()))
# new_price = []
# for i in range(n):
#     if i == 0:
#         new_price.append(int((price[i] + price[i + 1]) / 2))
#     elif i == n - 1:
#         new_price.append(int((price[i] + price[i - 1]) / 2))
#     else:
#         new_price.append(int((price[i] + price[i + 1] + price[i - 1]) / 3))
# print(" ".join(map(str,new_price)))

# 201809-2  买菜
n = int(input())

h_time = []
for i in range(n):
    h_time.append(list(map(int, input().split())))
w_time = []
for i in range(n):
    w_time.append(list(map(int, input().split())))
maxT = h_time[n - 1][1] if h_time[n - 1][1] > w_time[n - 1][1] else w_time[n - 1][1]
timeAxis = [0 for i in range(maxT + 1)]
for i in range(n):
    for j in range(h_time[i][0] + 1,h_time[i][1]+1):
        timeAxis[j] += 1
    for j in range(w_time[i][0] + 1,w_time[i][1]+1):
        timeAxis[j] += 1
#注意读题！！！
print(timeAxis.count(2))
