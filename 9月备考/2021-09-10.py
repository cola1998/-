# 201709-1 打酱油
# n = int(input())
# res = 0
# while n != 0:
#     if n>=50:
#         res += 7
#         n-=50
#     elif n>=30:
#         res += 4
#         n -= 30
#     else:
#         n -= 10
#         res += 1
# print(res)

# 201709-2 公共钥匙盒
# def findMinLocation():
#     for i in range(1, len(keys)):
#         if keys[i] == 0:
#             return i
#     return -1
#
#
# def findKeyLocation(key):
#     for i in range(1, len(keys)):
#         if keys[i] == key:
#             return i
#     return -1
#
#
# n, k = map(int, input().split())
# time_list = {}
# # time_list 的格式 {'1':[[1],[2]]}
# # 0维代表还 1维代表借
# time_key = []
# for i in range(k):
#     w, s, c = map(int, input().split())
#     if s not in time_list:
#         time_list[s] = [[], []]
#         time_list[s][1] = [w]
#         time_key.append(s)
#     else:
#         time_list[s][1].append(w)
#     if s + c not in time_list:
#         time_list[s + c] = [[], []]
#         time_list[s + c][0] = [w]
#         time_key.append(s + c)
#     else:
#         time_list[s+c][0].insert(0,w)
# keys = [i for i in range(n + 1)]
# time_key = sorted(time_key)
# print(time_list)
# for i in range(len(time_key)):
#     print(time_key[i],time_list[time_key[i]])
# for t in time_key:
#     # 每一时刻 先还
#     if len(time_list[t][0]) != 0:
#         time_list[t][0] = sorted(time_list[t][0])
#         for i in range(len(time_list[t][0])):
#             l = findMinLocation()
#             if l != -1:
#                 keys[l] = time_list[t][0][i]  # 还time_list[t][0][i]号钥匙
#     # 再借
#     if len(time_list[t][1]) != 0:
#         for i in range(len(time_list[t][1])):
#             l = findKeyLocation(time_list[t][1][i])
#             if l != -1:
#                 keys[l] = 0
#     print(" ".join(map(str, keys)))
# keys.pop(0)
# print(" ".join(map(str, keys)))


# 201703-1  分蛋糕
# n,k = map(int,input().split())
# weight = list(map(int,input().split()))
# res = 0
# count = 0
# i = 0
# while n > 0:
#     count += weight[i]
#     if count < k and n == 1:
#         res += 1
#         break
#     elif count < k:
#         i += 1
#         n -= 1
#     else:
#         count = 0
#         i += 1
#         res += 1
#         n -= 1
# print(res)

# 201703-2  学生排队
n = int(input())
m = int(input())
l = [i for i in range(n+1)]
for i in range(m):
    p,q = map(int,input().split())
    l0 = l.index(p)
    l.pop(l0)
    l0 += q
    l.insert(l0,p)
l.pop(0)
print(" ".join(map(str,l)))