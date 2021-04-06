#202012-1
# n = int(input())
# sum_s = 0
# for i in range(n):
#     w,score = map(int,input().split())
#     sum_s += (w*score)
# if sum_s < 0:
#     print(0)
# else:
#     print(sum_s)

#202212-2
m = int(input())
info = {}
keys = []
for i in range(m):
    y,result = map(int,input().split())
    if y not in keys:
        keys.append(y)
        info[y] = [0,0]
    if result == 0:
        info[y][0] += 1
    else:
        info[y][1] += 1
keys = sorted(keys)
#正反遍历两次求解  前缀和
info_0 = []
count = 0
for i in range(len(keys)):
    count += info[keys[i-1]][0]
    info_0.append(count)

#反向遍历
info_1 = []
count = 0
for j in range(len(keys)-1,-1,-1):
    count += info[keys[j]][1]
    info_1.append(count)
info_1 = info_1[::-1]

max = 0
k = -1
for i in range(len(keys)):
    count = info_0[i]+info_1[i]
    if count >= max:
        max = count
        k = i
print(keys[k])