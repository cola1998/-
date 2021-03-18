#201909-1
# n,m = map(int,input().split())
# info = []
# maxi,max = 0,0
#
# for i in range(n):
#     l = list(map(int,input().split()))
#     sumi = 0
#     for j in range(1,1+m):
#         sumi += abs(l[j])
#     if sumi > max:
#         max = sumi
#         maxi = i
#     info.append(l[0]-sumi)
# print("{0} {1} {2}".format(sum(info),maxi+1,max))

#201909-2
# n = int(input())
# T = 0 #记录所有果树的剩余果子数之和
# tag = [i*0 for i in range(n)]  #tag用于记录该棵树是否掉果，0表示未掉，1表示掉了
# for i in range(n):
#     l = list(map(int,input().split()))
#     total = 0
#     for j in range(1,l[0]+1):
#         if l[j] > 0:
#             if total == 0:
#                 total = l[j]
#             elif total > l[j]:
#                 tag[i] = 1
#                 total = l[j]
#             else:
#                 pass
#         else:
#             total -= abs(l[j])
#     T += total
# e = 0
# for i in range(n):
#     if i == 0 and tag[n-1] == 1 and tag[i] == 1 and tag[i+1] == 1:
#         e += 1
#         continue
#     if i == n-1 and tag[0] == 1 and tag[i] == 1 and tag[i-1] == 1:
#         e += 1
#         continue
#     if tag[i-1] == 1 and tag[i] == 1 and tag[i+1] == 1:
#         e += 1
#         continue
# print("{0} {1} {2}".format(T,sum(tag),e))

#201909-3
