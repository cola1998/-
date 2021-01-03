# 笔记 4.1.2 插入排序  小到大顺序
# A = input().split(' ')
# A = list(map(int,A))
# for i in range(len(A)):
#     x = A[i]
#     j=i-1
#     while j>=0 and A[j]>x:
#         A[j+1] = A[j]
#         j -= 1
#     A[j+1] = x
# print(A)

#假币问题 3 12 0  计算比较次数
# n = input().split()
# n = list(map(int,n)) #硬币个数
# times = [] #记录最多需要寻找的次数
#
# for i in range(len(n)):
#     count = 0
#     if(n[i]==0):
#         times.append(count)
#     else:
#         while(n[i]>1):
#             count += 1
#             n[i] = int(n[i]/3) + (n[i]%3>0)
#         times.append(count)
# print(times)

#B1032
# from collections import defaultdict  // 最后一个测试样例超时
# from functools import reduce
# N = int(input())
# keys = []
# infor = defaultdict(list)
# for i in range(N):
#     l = input().split(' ')
#     l = list(map(int,l))
#     infor[l[0]].append(l[1])
#     if l[0] not in keys:
#         keys.append(l[0])
#
# max = 0
# for i in range(len(keys)):
#     value = reduce(lambda x,y:x+y,infor[keys[i]])
#     if value>max:
#         max=value
#         k = keys[i]
# print("{0} {1}".format(k,max))
#
# import copy
# N = int(input())
# infor = {}
# max = 0
# k = -1
# for i in range(N):
#     l = input().split(' ')
#     t = int(l[0])
#     if t in infor:
#         infor[t]+=int(l[1])
#     else:
#         infor[t]=int(l[1])
#     if infor[t] > max:
#         max = infor[t]
#         k = copy.copy(t)
#
# print("{0} {1}".format(k,max))

#A1011 W T L
# n = []
# name_max = []
# nn = ['W','T','L']
# profit = 1
# for i in range(3):
#     l = input().split(' ')
#     l = list(map(float,l))
#     max_n = max(l)
#     n.append(max_n)
#     name_max.append(nn[l.index(max_n)])
# profit = (n[0]*n[1]*n[2]*0.65 - 1) * 2
# print("{0} {1} {2} {3}".format(name_max[0],name_max[1],name_max[2],round(profit,2)))

#A1006 找开门和关门的人
# N = int(input())
# n_list = []
# early_time = '240000'
# early_name = ''
# late_time = '000000'
# late_name = ''
# for i in range(N):
#     l = input().split(' ')
#     l[1].replace(':','')
#     l[2].replace(':', '')
#     if l[1]<early_time:
#         early_time=l[1]
#         early_name = l[0]
#     if l[2]>late_time:
#         late_time = l[2]
#         late_name = l[0]
# print("{0} {1}".format(early_name,late_name))

#A1036 name gender ID grade  输出女生最高分 和男生最低分 以及分数差
# N = int(input())
# n_list = []
# max_grade = 0
# tag_F = -1
# tag_M = -1
# min_grade = 100
# for i in range(N):
#     l = input().split(' ')
#     if l[1] == 'M':
#         tag_M = 1
#         if int(l[3]) <= min_grade:
#             min_grade = int(l[3])
#             min_name = l[0]
#             min_id = l[2]
#     else:
#         tag_F = 1
#         if int(l[3]) >= max_grade:
#             max_grade = int(l[3])
#             max_name = l[0]
#             max_id = l[2]
# if tag_F == -1:
#     print("Absent")
# else:
#     print("{0} {1}".format(max_name, max_id))
# if tag_M == -1:
#     print("Absent")
# else:
#     print("{0} {1}".format(min_name, min_id))
# if tag_M== -1 or tag_F==-1:
#     print("NA")
# else:
#     print(max_grade-min_grade)

#B1027
# def nn():
#     print()
# def kk(n,c):
#     for i in range(n):
#         print("{0}".format(c),end='')
# if __name__ == '__main__':
#     l = input().split(' ')
#     n = int(l[0])
#     c = l[1]
#     sum = 1
#     count = 1
#     i = 1
#     while n>=sum:
#         sum += (i*2+1)*2
#         i += 1
#         count += 1
#
#     # print(i)
#     if n<sum:
#         sum -= ((count - 1) * 2 + 1) * 2
#         i -= 2
#     else:
#         i -= 1
#     max = 2*i+1
#     for j in range(i,-1,-1):
#         kk(int((max-(2*j+1))/2),' ')
#         kk((2*j+1),c)
#         nn()
#     for j in range(1,i+1):
#         kk(int((max - (2 * j + 1)) / 2), ' ')
#         kk((2 * j + 1), c)
#         nn()
#     print(n-sum)

#A1031
# def kk(n,c):
#     for i in range(n):
#         print("{0}".format(c),end='')
# if __name__ == '__main__':
#     s = input()
#     N = len(s)
#     n2=0
#     max = 0
#     for i in range(1,int((N+2)/3)+1):
#         n2 = N-2*i+2
#         if (n2<i):
#             break
#         else:
#             max=i
#     n2 = N-2*max+2
#     # print(max,n2,max)
#     for i in range(1,max):
#         print(s[i-1],end='')
#         kk(n2-2,' ')
#         print(s[N-i])
#     print(s[max-1:max-1+n2])

#计数排序
A = input().split(' ')
A = list(map(int,A))
count = [i*0 for i in range(len(A))]
S = [i*0 for i in range(len(A))]
for i in range(len(A)-1):
    for j in range(i+1,len(A)):
        if(A[i]<A[j]):
            count[j] += 1
        else:
            count[i] += 1
print(count)
for i in range(len(A)):
    S[count[i]] = A[i]

print(S)