#B1031 查验身份证
# N = int(input())
# q = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
# result = []
#
# zm = {'1':0,'0':1,'X':2,'9':3,'8':4,'7':5,'6':6,'5':7,'4':8,'3':9,'2':10}
#
# for i in range(N):
#     tag = 0
#     l = input()
#     sum = 0
#     for j in range(len(l)-1):
#         if(l[j]>='0' and l[j]<='9'):
#             sum += int(l[j])*q[j]
#         else:
#             tag = -1
#     Z = sum % 11
#     # print(zm[int(l[len(l)-1])])
#     if(tag==-1):
#         result.append(l)
#     elif(zm[l[len(l)-1]]!=Z):
#         result.append(l)
# if(len(result)==0):
#     print('All passed')
# else:
#     for j in range(len(result)):
#         print(result[j])

#B1002
# n = input()
# result = 0
# for i in range(len(n)):
#     result += int(n[i])
#
# ss = ['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
# result=str(result)
# for i in range(len(result)):
#     if i==len(result)-1:
#         print('{0}'.format(ss[int(result[i])]))
#     else:
#         print('{0}'.format(ss[int(result[i])]),end=' ')

#B1014
'''
读题一定要读懂，是位置相同的***
第一轮检查时 A-G 和 A-N要限定完整
'''
# l = []
# for i in range(4):
#     l.append(input())
# tag = -1
# result = []
# for i in range(len(l[0])):
#     if(len(result) == 0):
#         if(l[0][i]>='A' and l[0][i]<='G'):
#             if(l[1][i]==l[0][i]):
#                 result.append(l[0][i])
#                 continue
#     if(len(result)==1):
#         if((l[0][i]>='0' and l[0][i] <='9') or (l[0][i]>='A' and l[0][i]<='N')):
#             if (l[1][i] == l[0][i]):
#                 result.append(l[0][i])
#                 break
#
# day_list = {'A':'MON','B':'TUE','C':'WED','D':'THU','E':'FRI','F':'SAT','G':'SUN'}
# hh_list = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23}
# tag = -1
# for i in range(len(l[2])):
#     if((l[2][i]>='a' and l[2][i]<='z')or(l[2][i]>='A' and l[2][i]<='Z')):
#         if(l[3][i]==l[2][i]):
#             tag = i
#             break
# tag = str(tag)
# while(len(tag)<2):
#     tag = '0' + tag
# hh = str(hh_list[result[1]])
# while(len(hh)<2):
#     hh = '0' +hh
# print("{0} {1}:{2}".format(day_list[result[0]],hh,tag))
#B1024
# x = input().split('.')
# if x[0][0]!='+':
#     result = x[0][0]
# else:
#     result = ''
# x[0] = x[0].strip('+-')
# for i in x[1].split('E'):
#     x.append(i)
# x.pop(1)
# if(x[2][0] == '-'):
#     #小数点左移
#     x[2] = x[2].strip('-')
#     while(len(x[0])<int(x[2])):
#         x[0] = '0' + x[0]
#     x[0] = '0.' + x[0]
#     result = result + x[0] + x[1]
#     print(result)
# else:
#     #小数点右移
#     x[2] = x[2].strip('+')
#     if(len(x[1])>int(x[2])):
#         x[0] = x[0] + x[1][:int(x[2])]
#         result = result + x[0] +'.'+ x[1][int(x[2]):]
#     elif(len(x[1])==int(x[2])):
#         x[0] = x[0]+x[1]
#         result = result + x[0]
#     else:
#         while(len(x[1])<int(x[2])):
#             x[1] = x[1] + '0'
#         x[0] = x[0] + x[1]
#         result = result + x[0]
#     print(result)
#B1048
l = input().split(' ')
result = ''
t = ['J','Q','K']
if(len(l[1])>len(l[0])):
    r = ''
    for j in range(len(l[1])-len(l[0])):
        r = r +'0'
    l[0] = r+l[0]
elif(len(l[1])<len(l[0])):
    r = ''
    for j in range(len(l[0]) - len(l[1])):
        r = r + '0'
    l[1] = r + l[1]
'''
因为我是从len-1 至 0位 所以i表示位数是不准的 要用j来单独表示一下
还要注意位数不同需要补零进行运算，而不能直接截取
'''
j = 0
for i in range(len(l[1])-1,-1,-1):
    if(j%2!=0):
        x = int(l[1][i]) - int(l[0][i])
        if (x < 0):
            x = x + 10
        result = str(x) + result
    else:
        x = (int(l[1][i]) + int(l[0][i])) % 13
        if (x >= 10):
            x = t[x - 10]
            result = x + result
        else:
            result = str(x) + result
    j += 1
print(result)