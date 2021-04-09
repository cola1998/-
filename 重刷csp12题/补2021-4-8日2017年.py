#201712-1
# n = int(input())
# l = list(map(int,input().split()))
# l = sorted(l)
# min = 99999
# for i in range(1,n):
#     if abs(l[i]-l[i-1])<min:
#         min = abs(l[i]-l[i-1])
# print(min)

#201712-2
# n,k = map(int,input().split())
# number = 0 #记录现在数到几了
# tag = [1 for i in range(n)]
# x = 0
# while sum(tag) != 1:
#     if tag[x] != 0:
#         number += 1
#         if number%k==0 or str(number)[-1] == str(k):
#             tag[x] = 0
#     x = (x+1)%n
# print(tag.index(1)+1)

#201709-1
# import math
# n = int(input())
# count = 0
# while n!=0:
#     if n >= 50:
#         c = math.floor(n/50)
#         count += (c*7)
#         n -= c*50
#     elif n>=30:
#         c = math.floor(n / 30)
#         count += (c * 4)
#         n -= c * 30
#     else:
#         c = math.floor(n / 10)
#         count += (c*1)
#         n -= c*10
# print(count)

#201709-2
# n,k = map(int,input().split())
# keys = [i for i in range(1,n+1)]
# time_list = []
# schedule = {}
# #True借 False还
# for i in range(k):
#     w,s,c = map(int,input().split())
#     if s not in time_list:
#         time_list.append(s)
#     if s+c not in time_list:
#         time_list.append(s+c)
#     if s in schedule:
#         schedule[s].append([w,True])
#     else:
#         schedule[s] = [[w,True]]
#     if s+c in schedule:
#         schedule[s+c].append([w, False])
#     else:
#         schedule[s+c] = [[w, False]]
# time_list = sorted(time_list)
# for time in time_list:
#     schedule[time] = sorted(schedule[time],key=lambda x:(x[1],x[0]))
#     for t in schedule[time]:
#         if t[1] == False:  #还
#             keys[keys.index(0)] = t[0]
#         elif t[1] == True: #借
#             keys[keys.index(t[0])] = 0
# print(" ".join(map(str,keys)))

#201703-1
# n,k = map(int,input().split())
# l = list(map(int,input().split()))
# count = 0
# now_weight = 0
# for i in range(n):
#     now_weight += l[i]
#     if now_weight < k and i == n-1: #如果到了最后一个人，但是没有分够也要加上
#         count += 1
#     elif now_weight < k:
#         pass
#     else:
#         count += 1
#         now_weight = 0
# print(count)

#201703-2
n = int(input())
m = int(input())
students = [i for i in range(1,n+1)]
info = []
for i in range(m):
    p,q = map(int,input().split())
    s = students.index(p)
    if s+q == n:
        students.remove(p)
        students.append(p)
    elif s+q == 0:
        students.remove(p)  #remove值 pop位置
        students.insert(0,p)
    # else:
    #     students.remove(p)
    #     students.insert(s+q,p)
    elif q < 0:#向前
        for j in range(s-1,s+q,-1):
            students[j+1] = students[j]
        students[s + q+1] = p
    else:#向后
        for j in range(s,s+q):
            students[j] = students[j+1]
        students[s + q] = p
print(" ".join(map(str,students)))