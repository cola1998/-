# A1001
# l = input().split(' ')
# sum = int(l[0]) + int(l[1])
# result = ''
# tag = ''
# if(sum<0):
#     sum = -sum
#     tag = '-'
# sum = str(sum)
# n = len(sum)
# for i in range(n-1,-1,-3):
#     if(i-2>-1):
#         result = ','+sum[i-2:i+1] + result
# if(n%3!=0):
#     result = tag + sum[:n%3] + result
# else:
#     result = tag + result[1:len(result)]
# print(result)

# A1005
# x = input()
# sum = 0
# for i in range(len(x)-1,-1,-1):
#     sum += int(x[i])
# print(sum)
# d = ['zero','one','two','three','four','five','six','seven','eight','nine']
# sum = str(sum)
# for i in range(len(sum)):
#     if i != len(sum)-1:
#         print(d[int(sum[i])],end=' ')
#     else:
#         print(d[int(sum[i])])

# A1035
# def check(s,d):
#     if(s in d):
#         return s
#     else:
#         return -1
# N = int(input())
# L = {}
# sum = 0
# replace_l = {'1':'@','0':'%','l':'L','O':'o'}
# modified = {}
# for i in range(N):
#     l = input().split(' ')
#     tag = 0
#     for j in range(len(l[1])):
#         if(check(l[1][j],replace_l)!=-1):
#             l[1] = l[1][0:j] + replace_l[l[1][j]] + l[1][j+1:]
#             tag = 1
#     if(tag == 1):
#         sum += 1
#         modified[l[0]] = l[1]
# if(sum==0 and N!=1):
#     print("There are {0} accounts and no account is modified".format(N))
# elif (sum == 0 and N==1):
#     print("There is 1 account and no account is modified")
# else:
#     print(sum)
#     for key,value in modified.items():
#         print("{0} {1}".format(key,value))

# A1077 最长公共后缀
# def reserveS(s):
#     result = ''
#     for i in range(len(s)):
#         result = s[i] + result
#     return result
#
# N = int(input())
# minLen = 999
# lists = []
# for i in range(N):
#     l = input()
#     if(len(l)<minLen):
#         minLen = len(l)
#     lists.append(reserveS(l))
# result = ''
# for i in range(minLen):
#     tag = -1
#     v = lists[0][i]
#     for j in range(1,len(lists)):
#         if(lists[j][i]==v):
#             tag = 0
#         else:
#             tag = -1
#             break
#     if(tag==0):
#         result=lists[0][i]+result
#     else:
#         break
# if(result==''):
#     print('nai')
# else:
#     print(result)

# A1082
x = input()
tag = ''
if (x[0] == '-'):
    tag = '-'
    x = x[1:]
    print(x)

digit = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
danwei = ['Shi', 'Bai', 'Qian', 'Wan', 'Yi']

result = ''
k = 0
for i in range(len(x) - 1, -1, -3):

    if (i == 0):
        result = digit[int(x[i])] + ' ' + result
    elif (i % 4 == 0 and result != ''):
        result = ' ' + digit[int(x[i])] + ' ' + result
    elif (i % 4 == 0):
        result = ' ' + digit[int(x[i])]
    else:
        if (k <= 2):
            result = ' ' + digit[int(x[i])] + ' ' + danwei[k] + result
        else:
            result = ' ' + digit[int(x[i])] + ' ' + danwei[k - 3] + result
        k += 1
        if (k == 2):
            result = ' ' + danwei[3] + result
        elif (k == 5):
            result = ' ' + danwei[4] + result
print(tag + result)
