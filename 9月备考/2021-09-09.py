# 201803-1 跳一跳
# l = list(map(int,input().split()))
# res = 0
# tag = 0
# for i in range(len(l)):
#     if l[i] == 0:
#         break
#     elif l[i] == 1:
#         tag = 0
#         res += 1
#     else:
#         tag += 1
#         res += (2*tag)
# print(res)

# 201803-2 碰撞的小球
# n, L, t = map(int, input().split())
# l = list(map(int,input().split()))  #初始位置数组
# l_2 = sorted(l)
# d = {}
# for i in range(len(l)):
#     d[i] = l_2.index(l[i])  #对应关系 l中第i个元素 对应l_2中的位置index i:index
# f = [1 for i in range(len(l_2))]  #记录小球的方向  初始全部为向右
# if l_2[-1] == L:
#     f[-1] = -1 #检查最后一个小球是否在最尾端位置
# for tt in range(t):#模拟t个时刻
#     for i in range(len(l_2)):#遍历每个小球
#         #  需要处理的特殊情况
#         if l_2[i] == 0:#抵达最左边
#             f[i] = 1
#             l_2[i] = 1 #改变方向后立即移动
#         elif l_2[i] == L:#抵达最右边
#             f[i] = -1
#             l_2[i] = L-1
#         elif i != len(l)-1 and l_2[i] == l_2[i+1] :
#             f[i] = (-1*f[i])
#             l_2[i] += f[i] * 1
#             f[i+1] = (-1*f[i+1])
#         else:
#             l_2[i] += f[i] * 1
# for i in range(len(l_2)):
#     if i != len(l_2)-1:
#         print(l_2[d[i]],end=" ")
#     else:
#         print(l_2[d[i]])
# 201712-1 最小差值
# n = int(input())
# l = list(map(int,input().split()))
# res = 99999
# l = sorted(l)
# for i in range(1,len(l)):
#     res = min(res,l[i]-l[i-1])
# print(res)

# 201712-2 游戏
n,k = map(int,input().split())
flag_l = [True for i in range(n+1)]  # 代表玩家是否被淘汰 False-被淘汰
flag_l[0] = False
num = 1  #记录当前的数
i = 1 # 记录当前到第几个小朋友了
while flag_l.count(True) != 1:
    if num % k == 0 or str(num)[-1] == str(k):
        flag_l[i] = False
    num += 1
    i += 1
    if i > n:
        i = i % n
    while flag_l[i] == False:
        i += 1
        if i > n:
            i = i%n
print(flag_l.index(True))