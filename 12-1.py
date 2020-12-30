#3n+1猜想
# step = 0 #用于记录除法步数
# n = int(input())
# while n!=1:
#     if(n%2 == 0):
#         n = n/2
#         print(n)
#     else:
#         n = (3*n+1)/2
#         print(n)
#     step+=1
#
# print('step=',step)

# from collections import defaultdict
# N = int(input())
# ll = defaultdict(int)
# MAX = 0
# max_index = 0
# for i in range(0,N):
#     s = input()
#     ls = s.split(' ')
#     ll[ls[0]] += int(ls[1])
#     if ll[ls[0]] > MAX:
#         MAX = ll[ls[0]]
#         max_index = ls[0]
# print('{0} {1}'.format(max_index,MAX))

# n = int(input())
# n_list = input().split(' ')
#
# x = int(input())
# tag = 0
# for i in range(n):
#     if x == int(n_list[i]):
#         tag = 1
#         print(i+1)
#         break
# if tag == 0:
#     print(-1)
l = input().split(' ')
N = int(l[0])
C = l[1]
if N%2 != 0:
    l = (N+1)/2
else:
    l = (N/2)
for i in range(int(l)):
    for j in range(N):
        if i==0 or i==int(l)-1:
            print(C,end='')
        else:
            if j == 0 or j == N-1:
                print(C,end='')
            else:
                print(' ',end='')
    print()