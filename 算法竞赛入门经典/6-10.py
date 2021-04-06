#例题5
# m = int(input())
# for i in range(m):
#     L,T,n = map(int,input().split())
#     direction_old = [1 for x in range(n)] #初始化方向都设为向右
#     l_old = [] #记录原来的顺序
#     for j in range(n):
#         l,d = input().split()
#         if d == 'L':
#             direction_old[j] = -1
#         l_old.append(int(l))
#
#     l = sorted(l_old)
#     order = []
#     direction = []
#     for j in range(len(l)):
#         x = l_old.index(l[j])
#         order.append(x)
#         direction.append(direction_old[x])
#     del(direction_old)
#     del(l_old)
#     tag = [0 for i in range(n)]
#     for j in range(T):
#         for p in range(len(l)):
#             if direction[p] != 0:
#                 l[p] += direction[p]
#             else:
#                 break
#             if l[p] > L or l[p] < 0:
#                 direction[p] = 0
#             elif l[p] == l[p-1]:
#                 if j == T-1:
#                     tag[p] = 1
#                     tag[p-1] = 1
#                 direction[p] = (-1)*direction[p]
#                 direction[p-1] = (-1) * direction[p-1]
#             elif l[p]<l[p-1] and p!=0:
#                 direction[p] = (-1) * direction[p]
#                 direction[p - 1] = (-1) * direction[p - 1]
#                 l[p-1] += direction[p-1]
#                 l[p] += direction[p]
#
#     print("Case #{0}:".format(i+1))
#     for j in range(n):
#         x = order.index(j)
#         if direction[x] == 0:
#             print("{0}".format("Fell off"))
#         elif tag[x] == 1:
#             print("{0} {1}".format(l[x],"Turning"))
#         elif direction[x] == -1:
#             print("{0} {1}".format(l[x],'L'))
#         else:
#             print("{0} {1}".format(l[x],'R'))
'''
2
10 1 4
1 R
5 R
3 L
10 R
10 2 3
4 R
5 L
8 R
'''

# m = int(input())
# for i in range(m):
#     L,T,n = map(int,input().split())
#     direction_old = [1 for x in range(n)] #初始化方向都设为向右
#     l_old = [] #记录原来的顺序
#     for j in range(n):
#         l,d = input().split()
#         if d == 'L':
#             direction_old[j] = -1
#         l_old.append(int(l))
#     #进行记录调整  这里应该可以简化的（参考书上）
#     l = sorted(l_old)
#     order = []
#     direction = []
#     for j in range(len(l)):
#         x = l_old.index(l[j])
#         order.append(x)
#         direction.append(direction_old[x])
#     del(direction_old)
#     del(l_old)
#     tag = [0 for i in range(n)]
#
#     for p in range(n):
#         if direction[p] != 0:
#             l[p] += direction[p]*T
#         else:
#             break
#         if l[p] > L or l[p] < 0:
#             direction[p] = 0
#         elif l[p] == l[p-1]:
#             tag[p] = 1
#             tag[p-1] = 1
#             direction[p] = (-1)*direction[p]
#             direction[p-1] = (-1) * direction[p-1]
#         elif l[p]<l[p-1] and p!=0:  #如果穿墙而过 ，直接调换二者方向和对应距离
#             direction[p] = (-1) * direction[p]
#             direction[p - 1] = (-1) * direction[p - 1]
#             temp = l[p-1]
#             l[p-1] = l[p]
#             l[p] = temp
#
#     print("Case #{0}:".format(i+1))
#     for j in range(n):
#         x = order.index(j)
#         if direction[x] == 0:
#             print("{0}".format("Fell off"))
#         elif tag[x] == 1:
#             print("{0} {1}".format(l[x],"Turning"))
#         elif direction[x] == -1:
#             print("{0} {1}".format(l[x],'L'))
#         else:
#            print("{0} {1}".format(l[x],'R'))

#例题6 给定视图，判断重量  ????
# n = int(input())
# #前 左 后 右 顶 底
# info = []
# for i in range(n):
#     info.append(input().split())

#例题7
from sortedcontainers import SortedList

def find132pattern(nums):
    n = len(nums)
    if n < 3:
        return False

    # 左侧最小值
    left_min = nums[0]
    # 右侧所有元素
    right_all = SortedList(nums[2:])

    for j in range(1, n - 1):
        if left_min < nums[j]:
            index = right_all.bisect_right(left_min)
            if index < len(right_all) and right_all[index] < nums[j]:
                return True
        left_min = min(left_min, nums[j])
        right_all.remove(nums[j + 1])

    return False

result = find132pattern([1,2,3,4])
print(result)