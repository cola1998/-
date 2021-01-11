#A1016 借鉴别人的代码
'''
学习到
1、可以直接使用sorted函数进行排序 无需自己再写代码进行排序操作
2、字符串也可以用格式化"{} {}".format()
3、显示小数点后两位也可以用格式化"{:.2f}.format()"
4、计算时间和金额可以将time1和time2计算从00:00:00:00开始的金额，然后相减，这样可以减少计算跨天等等麻烦
'''
# def telephone():
#     line = input().split(" ")
#     rate = [int(x) for x in line]
#     oneday = sum([x for x in rate])*60
#     num = int(input())
#     record = {}
#     for x in range(num):
#         line = input().split(' ')
#         if line[0] in record:
#             record[line[0]].append(line[1:])
#         else:
#             record[line[0]] = [line[1:]]
#     name = sorted(record.keys())
#     for x in name:
#         unit = sorted(record[x])
#         bill = []
#         stack = []
#         for i in unit:
#             if len(stack) == 0:
#                 if i[1] == 'on-line':
#                     stack.append(i)
#             else:
#                 if i[1] == stack[0][1]:
#                     stack[0]=i
#                 else:
#                     bill.append([stack[0],i])
#                     stack = []
#         if len(bill)>0:
#             count = 0
#             result = '{} {}\n'.format(x,bill[0][0][0][:2])
#             for i in bill:
#                 start = i[0][0]
#                 end = i[1][0]
#                 result = result +start[3:]+' '+end[3:]+' '
#                 m1,m2 = 0,0
#                 day1,day2 = int(start[3:5]),int(end[3:5])
#                 hour1,hour2 = int(start[6:8]),int(end[6:8])
#                 minute1,minute2 = int(start[9:11]),int(end[9:11])
#
#                 m1 = oneday*day1+sum(rate[:hour1])*60 + rate[hour1]*int(minute1)
#                 m2 = oneday*day2 + sum(rate[:hour2])*60 + rate[hour2]*int(minute2)
#
#                 time = (day2-day1)*24*60 + (hour2-hour1)*60 + minute2-minute1
#                 result = result+str(time)+' '
#                 m = m2-m1
#                 result = result+'$'+'{:.2f}'.format(m/100)+'\n'
#                 count += m
#             result = result + 'Total amount: ${:.2f}'.format(count/100)
#             print(result)

#A1028
'''
又是借鉴大神代码的一天
学习到
1、sorted函数结合lambda排序 可以添加一个待排序列表和多个key
sorted(list,key = lambda x:(x1,x2))
2、可以直接使用字符串切片进行处理 避免了遍历数组等问题
[-2:] 最后两位
[6:-3]  第六位开始 到倒数第三位
最后输出也就直接输出字符串了 
3、避免惯性思维 害死人
发现python中sorted lambda 和字符串真是强大！
'''
# def listSorting():
#     line = input().split(' ')
#     N = int(line[0])
#     C = int(line[1])
#     '''
#     C=1 increasing ids
#     C=2 non-decreasing names
#     C=3 non-decreasing grades
#     '''
#     students = []
#     for i in range(N):
#         line = input()
#         students.append(line)
#
#     if(C==1):
#         students = sorted(students)
#     elif(C==2):
#         students = sorted(students,key = lambda x:(x[7:-3],x[:6]))
#     else:
#         students = sorted(students,key = lambda x:(x[-2:],x[:6]))
#     for x in students:
#         print(x)

'''
A1055
独立完成，但是有两个测试点超时
学习到如果待排序的要求顺序不一样（如一个要求从小到大、另一个要求从大到小），可以利用负号进行调整
大神的代码只有一个测试点超时  有时间可以学习一下

'''
# import copy
# def WorldRichest():
#     line = input().split(' ')
#     N = int(line[0])
#     K = int(line[1])
#     users = []
#     query = []
#     for i in range(N):
#         linen = input().split(' ')
#         line = [linen[0],int(linen[1]),int(linen[2])]
#         users.append(line)
#     #先对users进行按照年纪/财富值进行排序 每个年龄只取前100名
#     users = sorted(users,key=lambda x:(-x[2],x[1],x[0]))
#
#     for i in range(K):
#         line = input().split(' ')
#         line = list(map(int,line))
#         query.append(line)
#     for i in range(len(query)):
#         number = query[i][0]
#         print("Case #{}:".format(i+1))
#         k = copy.copy(number)
#         for j in range(len(users)):
#             if int(users[j][1])>=query[i][1] and int(users[j][1])<=query[i][2] and number>0:
#                 print("{0} {1} {2}".format(users[j][0],users[j][1],users[j][2]))
#                 number -= 1
#                 if number == 0:
#                     break
#         if(number == k):
#             print("None")

#B1029
# def keyboard():
#     l = input()
#     l2 = input()
#     l = l.upper()
#     l2 = l2.upper()
#     result = ''
#     HashTable = [i*0 for i in range(128)]
#     for i in range(len(l)):
#         if(l[i] in l2):
#             pass
#         else:
#             if(HashTable[ord(l[i])] == 0):
#                 result = result + l[i]
#                 HashTable[ord(l[i])] = 1
#             else:
#                 pass
#     print(result)

#b1033
'''
测试样例：
AC
aAbBcCdD
输出
bBdD
'''
# def keyboard2():
#     l = input() #输入坏的键
#     l2 = input() #输入要输出的句子
#     l = l.lower()
#     upper_tag = 0
#     result = ''
#     HashTable = [i*0 for i in range(128)]
#     for i in range(len(l)):
#         if(HashTable[ord(l[i])] == 0):
#             HashTable[ord(l[i])] = 1  #将不能用的置为1
#             HashTable[ord(l[i])-32] = 1
#         if(l[i] == '+'):
#             upper_tag = 1
#     for i in range(len(l2)):
#         if(HashTable[ord(l2[i])]==1):
#             pass
#         else:
#             if(upper_tag==1 and l2[i].isupper()):
#                 pass
#             else:
#                 result = result+l2[i]
#     print(result)

#B1038
def Score():
    n = int(input())
    l = input().split(' ')
    q = input().split(' ')
    hashTable = [i*0 for i in range(101)]
    for i in range(len(l)):
        hashTable[int(l[i])] += 1
    result = []
    for j in range(1,len(q)):
        result.append(str(hashTable[int(q[j])]))
    print(" ".join(result))

if __name__ == '__main__':
    # telephone()
    # listSorting()
    # WorldRichest()
    # keyboard()
    # keyboard2()
    Score()