# A1082  待修改
# x = input()
# tag = ''
# if(x[0]=='-'):
#     tag = '-'
#     x = x[1:]
#     print(x)
#
# digit = ['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
# danwei = ['Shi','Bai','Qian','Wan','Yi']
#
# result = ''
# k = 0
# for i in range(len(x)-1,-1,-3):
#
#     if(i==0):
#         result = digit[int(x[i])] + ' ' + result
#     elif (i%4==0 and result!=''):
#         result = ' ' + digit[int(x[i])] + ' ' + result
#     elif (i%4==0):
#         result = ' ' + digit[int(x[i])]
#     else:
#         if(k<=2):
#             result = ' ' + digit[int(x[i])] +' ' +danwei[k]+ result
#         else:
#             result = ' ' + digit[int(x[i])] + ' ' + danwei[k-3] + result
#         k += 1
#         if(k==2):
#             result = ' ' + danwei[3]+result
#         elif (k==5):
#             result = ' ' + danwei[4] + result
# print(tag+result)

# 排序
'''
1、选择排序
2、直接插入排序
'''


# def selectSort(L):
#     for i in range(len(L)):
#         min = i
#         for j in range(i,len(L)):
#             if(L[j]<L[min]):
#                 min = j
#         temp = L[i]
#         L[i] = L[min]
#         L[min] = temp
#     return L
# def insertSort(L):
#     for i in range(1,len(L)):
#         v = L[i]
#         j = i
#         while j>0 and L[j-1]>v:
#             L[j] = L[j-1]
#             j -= 1
#         L[j] = v
#     return L

# B1015  超时
# def cmp(a,b):
#     #1 表示a大  -1表示b大
#     if(a['flag'] != b['flag']):
#         if(a['flag']<b['flag']):
#             return 1
#         else:
#             return -1
#     else:
#         if(a['de']+a['ca'] != b['de']+b['ca']):
#             if(a['de']+a['ca'] > b['de']+b['ca']):
#                 return 1
#             else:
#                 return -1
#         else:
#             if(a['de'] != b['de']):
#                 if(a['de']>b['de']):
#                     return 1
#                 else:
#                     return -1
#             else:
#                 if(a['id']<b['id']):
#                     return 1
#                 else:
#                     return -1
#
# l = input().split(' ')
# N = int(l[0])
# L = int(l[1])
# H = int(l[2])
# M = 0
# students = []
# for i in range(N):
#     l = input().split(' ')
#     x = {'id':l[0],'de':int(l[1]),'ca':int(l[2])}
#     if(x['de']>=L and x['ca']>=L):
#         M += 1
#         if(x['de']>=H and x['ca']>=H):
#             x['flag'] = 1
#         elif(x['de']>=H and x['ca']<H):
#             x['flag'] = 2
#         elif(x['de']>x['ca'] and x['de']<H and x['ca']<H):
#             x['flag'] = 3
#         else:
#             x['flag'] = 4
#         students.append(x)
# print(M)
# for i in range(len(students)):
#     #冒泡排序
#     for j in range(len(students)-i-1):
#         if cmp(students[j],students[j+1])==-1:
#             temp = students[j]
#             students[j] = students[j+1]
#             students[j+1] = temp
# for i in range(len(students)):
#     print("{0} {1} {2}".format(students[i]['id'],students[i]['de'],students[i]['ca']))

# A1012
# def sort(L,key):
#     for i in range(len(L)):
#         j = i
#         v = L[i]
#         while j>0 and L[j-1][key]<v[key]:
#             L[j] = L[j-1]
#             j -= 1
#         L[j] = v
#
#     for i in range(len(L)):
#         if(i==0):
#             L[i][key + '_rank'] = 1
#         else:
#             if(L[i][key] == L[i-1][key]):
#                 L[i][key + '_rank'] = L[i-1][key+'_rank']
#             else:
#                 L[i][key + '_rank'] = i + 1
#     return L
# def find_min(L):
#     min = 0
#     for i in range(1,len(L)):
#         if(L[i]<L[min]):
#             min = i
#     return min
#
# def cmp(x):
#     a_rank = x['A_rank']
#     c_rank = x['C_rank']
#     m_rank = x['M_rank']
#     e_rank = x['E_rank']
#     L = [a_rank,c_rank,m_rank,e_rank]
#     tag = find_min(L)
#     if(tag == 0):
#         x['tag'] = str(x['A_rank']) + ' A'
#     elif(tag == 1):
#         x['tag'] = str(x['C_rank']) + ' C'
#     elif(tag==2):
#         x['tag'] = str(x['M_rank']) + ' M'
#     else:
#         x['tag'] = str(x['E_rank']) + ' E'
#     return x
#
# def find(students,x):
#     for i in range(len(students)):
#         if(students[i]['id']==x):
#             return i
#     return -1
#
# l  = input().split(' ')
# n = int(l[0])
# m = int(l[1])
# students = []
# q_list = []
#
# for i in range(n):
#     x = input().split(' ')
#     s = {'id':x[0],'C':int(x[1]),'M':int(x[2]),'E':int(x[3]),'A':int((int(x[1])+int(x[2])+int(x[3]))/3)}
#     students.append(s)
#
# for i in range(m):
#     q_list.append(input())
# students = sort(students,'C')
# students = sort(students,'M')
# students = sort(students,'E')
# students = sort(students,'A')
#
# for i in range(len(q_list)):
#     tag = find(students,q_list[i])
#     if(tag!=-1):
#         students[tag] = cmp(students[tag])
#         print("{0}".format(students[tag]['tag']))
#     else:
#         print('N/A')


# A1025
# 可以使用插入排序
# N = int(input()) #考点数
# testee_number = 0  #考生数量
# rank_list = []
#
# def cmp(v,k):
#     if(v['score']>k['score']):
#         return 1
#     elif(v['score']<k['score']):
#         return -1
#     else:
#         if(v['registration_number']<k['registration_number']):
#             return 1
#         else:
#             return -1
#
# for i in range(N):
#     K = int(input())
#     loc_rank_list = []
#     testee_number += K
#     for j in range(K):
#         l = input().split(' ') #注册号和分数
#         student = {'registration_number':l[0],'location_number':i+1,'score':int(l[1])}
#         loc_rank_list.append(student)
#         k = j
#         v = loc_rank_list[j]
#         while k>0 and loc_rank_list[k-1]['score']<v['score']:
#             loc_rank_list[k] = loc_rank_list[k-1]
#             k -= 1
#         loc_rank_list[k] = v
#     for s in range(len(loc_rank_list)):
#         if(s>=1):
#             if(loc_rank_list[s]['score']==loc_rank_list[s-1]['score']):
#                 loc_rank_list[s]['local_rank'] = loc_rank_list[s-1]['local_rank']
#             else:
#                 loc_rank_list[s]['local_rank'] = s+1
#         else:
#             loc_rank_list[s]['local_rank'] = s + 1
#         rank_list.append(loc_rank_list[s])
# for i in range(len(rank_list)):
#     k = rank_list[i]
#     j = i
#     while j>0 and cmp(rank_list[j-1],k)==-1:
#         rank_list[j] = rank_list[j-1]
#         j -= 1
#     rank_list[j] = k
# print(testee_number)
# for i in range(len(rank_list)):
#     if(i>=1):
#         if(rank_list[i]['score']==rank_list[i-1]['score']):
#             rank_list[i]['rank'] = rank_list[i-1]['rank']
#             print("{0} {1} {2} {3}".format(rank_list[i]['registration_number'],rank_list[i]['rank'],rank_list[i]['location_number'],rank_list[i]['local_rank']))
#         else:
#             rank_list[i]['rank'] = i+1
#             print("{0} {1} {2} {3}".format(rank_list[i]['registration_number'],rank_list[i]['rank'],rank_list[i]['location_number'],rank_list[i]['local_rank']))
#     else:
#         rank_list[i]['rank'] = i + 1
#         print("{0} {1} {2} {3}".format(rank_list[i]['registration_number'], rank_list[i]['rank'],
#                                        rank_list[i]['location_number'], rank_list[i]['local_rank']))

# A1016
def cmp(a, b):
    a = a.replace(':', '')
    b = b.replace(':', '')
    if (a[:2] != b[:2]):
        if (a[:2] > b[:2]):
            return 1
        else:
            return -1
    else:
        if (a[2:4] > b[2:4]):
            return 1
        elif (a[2:4] < b[2:4]):
            return -1
        else:
            if (a[4:6] != b[4:6]):
                if (a[4:6] > b[4:6]):
                    return 1
                else:
                    return -1
            else:
                if (a[6:] != b[6:]):
                    if (a[6:] > b[6:]):
                        return 1
                    else:
                        return -1
                else:
                    return 0


def calm(a, b, L):
    end_day = int(b[:2])
    end_hour = int(b[3:5])
    end_minute = int(b[6:])
    k = 0
    money = 0
    temp_day = int(a[:2])
    temp_hour = int(a[3:5])
    temp_minute = int(a[6:])
    while (temp_day < end_day or temp_hour < end_hour or temp_minute < end_minute):
        temp_minute += 1
        k += 1
        money += L[temp_hour]
        if (temp_minute >= 60):
            temp_minute = 0
            temp_hour += 1
        if (temp_hour >= 24):
            temp_hour = 0
            temp_day += 1
    return round(money, 2), k


from collections import defaultdict

l = input().split(' ')  # 代表每一时间段资费
l = list(map(int, l))
N = int(input())
info = defaultdict(list)
keys = []
for i in range(N):
    x = input().split(' ')
    v = x[0]
    x.pop(0)
    info[v].append(x)
for key in info.keys():
    keys.append(key)
keys.sort()
# 同一个用户按照时间顺序排列 检查顺序是否是online offline即可
for i in range(len(keys)):
    d = info[keys[i]]
    for j in range(len(d)):
        v = d[j]
        k = j
        while k > 0 and cmp(d[k - 1][0], v[0]) == 1:
            d[k] = d[k - 1]
            k -= 1
        d[k] = v
    info[keys[i]] = d
qualified_list = {}
for i in range(len(keys)):
    tag = 0
    qualified_list[keys[i]] = []
    for j in range(1, len(info[keys[i]])):
        if (info[keys[i]][j - 1][1] == 'on-line' and info[keys[i]][j][1] == 'off-line'):
            money, k = calm(info[keys[i]][j - 1][0][3:], info[keys[i]][j][0][3:], l)
            q = [info[keys[i]][j - 1][0][3:], info[keys[i]][j][0][3:], money / 100, info[keys[i]][j][0][:2], k]
            qualified_list[keys[i]].append(q)
for key in keys:
    print(key, qualified_list[key][0][3])
    sum = 0
    for i in range(len(qualified_list[key])):
        sum += qualified_list[key][i][2]
        print("{0} {1} {2} $".format(qualified_list[key][i][0], qualified_list[key][i][1], qualified_list[key][i][4]),
              end='')
        print("%.2f" % qualified_list[key][i][2])
    print("Total amount: $%.2f" % sum)
