#202012-1
# n = int(input())
# l = []
# sum = 0
# for i in range(n):
#     w,score = map(int,input().split())
#     sum += (w*score)
# print(max(0,sum))

#202012-2
# m = int(input())
# info = []
# xita = [] #记录θ的全部可取值
# for i in range(m):
#     x,re = map(int,input().split())
#     if x not in xita:
#         xita.append(x)
#     info.append([x,re])
# xita = sorted(xita)
# max = 0
# k = -1
# for i in xita:
#     count = 0
#     for j in info:
#         if j[0]>=i and j[1]==1:
#             count += 1
#         elif j[0]<i and j[1]==0:
#             count += 1
#     if count >= max:
#         max = count
#         k = i
# print(k)

# m = int(input())
# info_0 = []
# info_1 = []
# xita = [] #记录θ的全部可取值
# for i in range(m):
#     x,re = map(int,input().split())
#     if x not in xita:
#         xita.append(x)
#     if re == 0:
#         info_0.append(x)
#     else:
#         info_1.append(x)
# xita = sorted(xita)
# max = 0
# k = -1
# for i in xita:
#     count = 0
#     s = [x for x in info_0 if x<i]
#     count += len(s)
#     s = [x for x in info_1 if x >= i]
#     count += len(s)
#     if count >= max:
#         max = count
#         k = i
# print(k)
'''
前缀和思路！！！
参考了网上大神的代码
将θ可取值单独存放在xita列表中，并按照从小到大的顺序排列
并将其按照键值存储在字典dic中{0:[0,1],1:[1,1],...}
value一维数组*2代表得分为键值的 result为0有几个人 为1有几个人
相当于二维数组
  0  1
0
1
3
5
7
然后正向遍历dic[xita[i-1]][0] 统计小于θ的0的个数 (注意-1是因为是小于，需要错一位)
反向遍历dic[xita[i]][1] 统计大于等于θ的1的个数 ans1 = ans1[::-1] 将数组逆序调整过来
然后两个数组相加，记录最大的数max和位置k，输出对应的xita[k]值(注意和相同时，记录θ较大的那个)
'''
m = int(input())
dic = {}
xita = []
k = 0 #记录个数
for i in range(m):
    x,r = map(int,input().split())
    if x not in dic:
        dic[x] = [0,0]
        xita.append(x)
    if r == 0:
        dic[x][0] += 1
    else:
        dic[x][1] += 1
xita = sorted(xita)
#正向统计小于θ的0个数
ans = []
count = 0
for i in range(len(xita)):
    count += dic[xita[i-1]][0]
    ans.append(count)
print(ans)
#逆向统计大于θ的1个数
ans1 = []
count = 0
for i in range(len(xita)-1,-1,-1):
    count += dic[xita[i]][1]
    ans1.append(count)
ans1 = ans1[::-1]
print(ans1)
max = 0
k = 0
s = []
for i in range(len(ans)):
    ss = ans[i]+ans1[i]
    if ss >= max:
        max = ss
        k = i
print(xita[k])

# m = int(input())
# dic = {}  #装y和result
# res = []  #装不重复的y
# k = 0
# for i in range(m):
#     y,result = map(int,input().split())
#     if y not in dic:
#         dic[y] = [0,0]
#         if result == 0:
#             dic[y][0] += 1
#         else:
#             dic[y][1] += 1
#         res.append(y)
#         k += 1
#     else:
#         if result == 0:
#             dic[y][0] += 1
#         else:
#             dic[y][1] += 1
# res.sort()
# print(dic)
# order = 0
# ans = [0]  #装比这个数小的数的0的个数
# #利用前缀和顺序求
# for i in range(1,k):
#     print("res[i-1",res[i-1])
#     print('dic..',dic[res[i-1]][0])
#     order += dic[res[i-1]][0]
#     ans.append(order)
# order1 = 0
# ans1 = []  #装比这个数大的数的1的个数
# #利用前缀和倒序求
# for j in range(k-1,-1,-1):
#     order1 += dic[res[j]][1]
#     ans1.append(order1)
# ans1 = ans1[::-1]  #将数组所有元素逆置
# #统计预测正确的个数
# for i in range(k):
#     ans[i] += ans1[i]
# max1 = max(ans)
# for i in range(k-1,-1,-1):
#     if ans[i] == max1:
#         print(res[i])
#         break