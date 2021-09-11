# 201612-1 中位数
# n = int(input())
# l = list(map(int,input().split()))
# l = sorted(l)
# tag = 0
# for i in range(len(l)):
#     xn = l.index(l[i])
#     dn = 0
#     for j in range(xn,len(l)):
#         if l[j] > l[i]:
#             dn += 1
#     if xn == dn:
#         print(l[i])
#         tag = -1
#         break
# if tag == 0:
#     print(-1)

# 201609-1 最大波动
# n = int(input())
# l = list(map(int, input().split()))
# maxc = 0
# for i in range(1, len(l)):
#     if abs(l[i] - l[i - 1]) > maxc:
#         maxc = abs(l[i] - l[i - 1])
# print(maxc)


# 201609-2 火车购票
# def getLocation(q,location):
#     tag = -1
#     for i in range(len(l)):
#         if l[i] >= q:
#             tag = i
#             break
#     if tag != -1:#找到了相邻的几个座位
#         res = []
#         for j in range(len(location[tag])):
#             if location[tag][j] == 0:
#                 location[tag][j] = 1
#                 res.append(tag*5+j+1)
#                 q -= 1
#                 l[tag] -= 1
#                 if q == 0:
#                     return res
#     else:#没有相邻的座位
#         res = []
#         for i in range(20):
#             if l[i] > 0:
#                 for j in range(5):
#                     if location[i][j] == 0:
#                         location[i][j] = 1
#                         res.append(i * 5 + j + 1)
#                         q -= 1
#                         l[i] -= 1
#                         if q == 0:
#                             return res
#             else:
#                 pass
#
#
# n = int(input())
# location = [[0 for i in range(5)] for i in range(20)]
# l = [5 for i in range(20)]
# p = list(map(int, input().split()))
# for i in range(len(p)):
#     res = getLocation(p[i], location)
#     print(" ".join(map(str, res)))

# 经典数位DP问题
class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [0]*31
        dp[0] = 1
        dp[1] = 1
        for i in range(2,31):
            dp[i] = dp[i-1] + dp[i-2]

        pre = 0  # 记录上一层根节点值？
        res = 0  # 记录最终路径数
        for i in range(29,-1,-1):
            val = (1<<i)
            if n & val:
                #有右子树
                n -= val
                res += dp[i+1] #先将左子树的路径加到结果中
                if pre == 1:
                    break  #上一层为1 之后要处理的右子树根节点也为1 连续两个1 不满足题意
                pre = 1 #标记当前根节点为1
            else:
                # 无右子树，需要在下一层判断
                pre = 0
            if i == 0:
                res += 1
        return res