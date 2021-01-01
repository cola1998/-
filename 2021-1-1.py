#A1002 求两个多项式的和  -- 最后一个测试样例未通过
# from collections import defaultdict
# from functools import reduce
# l1 = input().split(' ')
# l2 = input().split(' ')
#
# l1 = list(map(float,l1))
# l2 = list(map(float,l2))
#
# num = defaultdict(list)
# for i in range(1,len(l1),2):
#     num[int(l1[i])].append(l1[i+1])
# for i in range(1,len(l2),2):
#     num[int(l2[i])].append(l2[i+1])
#
# keys = []
# values = []
#
# for key in num.keys():
#     keys.append(key)
# keys.sort(reverse=True)
#
# remain_list=[]
# for i in range(len(keys)):
#
#     value = reduce(lambda x, y: x + y, num[keys[i]])
#     if(value!=0):
#         values.append(round(value,1))
#         remain_list.append(keys[i])
#
#
# if len(remain_list) == 0:
#     pass
# else:
#     print(len(remain_list), end=' ')
#     for i in range(len(remain_list)):
#         print(remain_list[i], end=' ')
#         if i != len(remain_list) - 1:
#             print(values[i], end=' ')
#         else:
#             print(values[i])

#A1009
# from collections import defaultdict
# from functools import reduce
# l1 = input().split(' ')
# l2 = input().split(' ')
#
# l1 = list(map(float,l1))
# l2 = list(map(float,l2))
#
# n1 = {}
# n2 = {}
# for i in range(1,len(l1),2):
#     n1[int(l1[i])]=l1[i+1]
#
# for i in range(1,len(l2),2):
#     n2[int(l2[i])] = l2[i+1]
#
# keys = []
# temp = defaultdict(list)
#
# for item in n1.items():
#     key = item[0]
#     value = item[1]
#     for item2 in n2.items():
#         temp[key+item2[0]].append(value*item2[1])
# for key in temp.keys():
#     keys.append(key)
# keys.sort(reverse=True)
# remain_list = []
# values = []
#
# for i in range(len(keys)):
#     value = reduce(lambda x, y: x + y, temp[keys[i]])
#     if value != 0:
#         remain_list.append(keys[i])
#         values.append(round(value,1))
#
# print(len(remain_list),end=' ')
# for i in range(len(remain_list)):
#
#     if(i == len(remain_list)-1):
#         print("{0} {1}".format(remain_list[i],values[i]))
#     else:
#         print("{0} {1}".format(remain_list[i],values[i]),end=' ')

#B1041
# N = int(input())
# inf_list = {}
# for i in range(N):
#     l = input().split()
#     inf_list[int(l[1])] = [l[0],l[2]]
# M = int(input())
# find_list = input().split(' ')
# find_list = list(map(int,find_list))
#
# for i in range(len(find_list)):
#     print("{0} {1}".format(inf_list[find_list[i]][0],inf_list[find_list[i]][1]))

#B1004
# n = int(input())
# max = 0
# min = 999
# max_infor = []
# min_infor = []
# for i in range(n):
#     l = input().split(' ')
#     if(int(l[2])>max):
#         max=int(l[2])
#         max_infor=[l[0],l[1]]
#     if(int(l[2])<min):
#         min = int(l[2])
#         min_infor = [l[0],l[1]]
# print("{0} {1}".format(max_infor[0],max_infor[1]))
# print("{0} {1}".format(min_infor[0],min_infor[1]))

#B1028
N = int(input())

number = 0 #有效生日的个数

max_name = ""
min_name = ""
min_time = "18140906"
max_time = "20140906"
for i in range(N):
    l = input().split(' ')
    time = l[1].replace('/','')
    if(time >= "18140906" and time < "20140906"):
        number += 1
        if(time <= max_time):
            max_time=time
            max_name=l[0]
        if (time >= min_time):
            min_time = time
            min_name = l[0]
if number == 0:
    print(number)
else:
    print("{0} {1} {2}".format(number,max_name,min_name))

# 不超时版本
# import sys
#
# n=int(input())
#
# max_name=''
# min_name=''
# max_time='20140906'
# min_time='18140906'
#
# i=0
#
# for _ in range(n):
#     s=sys.stdin.readline()
#     time=s[-11:-7]+s[-6:-4]+s[-3:-1]
#     if time<'18140906' or time >'20140906':
#         continue
#     else:
#         i+=1
#         if time>min_time:
#             min_time=time
#             min_name=s[:-12]
#         if time<max_time:
#             max_time=time
#             max_name=s[:-12]
# if i==0:
#     print(i)
# else:
#     print(f'{i} {max_name} {min_name}')