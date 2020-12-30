#A1042 Shuffling Machine
# import copy
# K = int(input()) #表示重复两次
# l = input().split(' ') #contain given order
# start = [i for i in range(len(l))]
# next = []
# end = copy.copy(start)
# for j in range(K):
#     for i in range(len(l)):
#         next.append(int(l[i])-1)
#         end[next[i]] = start[i]
#     start = copy.copy(end)
# mp = ['S','H','C','D','J']
# for i in range(len(end)):
#     h = int((end[i]-1)/13)
#     if i != len(end)-1:
#         print("{0}{1} ".format(mp[h],((end[i]-1)%13 + 1)),end='')
#     else:
#         print("{0}{1}".format(mp[h], ((end[i] - 1) % 13 + 1)), end='')

# l = input().split(' ')
# N = int(l[0])
# D_list = [int(x) for x in l]
# D_list.pop(0)
# print(D_list)

#A1046
# l = input().split(' ')
# N = int(l[0])
# A = []
# dis = []
# sum = 0
# for i in range(1,len(l)):
#     sum += int(l[i])
#     dis.append(sum)
#     A.append(int(l[i]))
# M = int(input())
# for i in range(M):
#     q = input().split(' ')
#     l = []
#     for j in range(len(q)):
#         l.append(int(q[j]))
#     if(l[0] < l[1]):
#         if(l[0]!=1):
#             d1 = dis[l[1]-2]-dis[l[0]-2]
#         else:
#             d1 = dis[l[1]-2]
#         if(sum-d1<d1):
#             print(sum-d1)
#         else:
#             print(d1)
#     else:
#         if (l[1] != 1):
#             d1 = dis[l[0] - 2] - dis[l[1] - 2]
#         else:
#             d1 = dis[l[0] - 2]
#         if (sum - d1 < d1):
#             print(sum - d1)
#         else:
#             print(d1)

#A1065
# N = int(input())
# l = []
# for i in range(N):
#     temp_l = input().split(' ')
#     l.append(temp_l)
# for i in range(N):
#     if(int(l[i][0]) + int(l[i][1]) > int(l[i][2])):
#         print("Case #{0}: {1}".format(i+1,'true'))
#     else:
#         print("Case #{0}: {1}".format(i+1, 'false'))

#B1010
# l = input().split(' ')
# new_l = []
# for i in range(len(l)):
#     if(i%2 == 0):
#         x = int(l[i])*int(l[i+1])
#         print(x,end=' ')
#     else:
#         x = int(l[i]) - 1
#         if (x==0):
#             print(x)
#         else:
#             print(x,end=' ')
#
l = input().split(' ')
x = []
i = 0
while i<len(l)-1:
    m = int(l[i]) * int(l[i+1])
    n = int(l[i+1]) - 1
    i += 2
    if(n==-1):
        continue
    x.append(str(m))
    x.append(str(n))
if(len(x) == 0):
    print('0 0')
else:
    print(' '.join(x).strip())