# 2013-12-01
# n = int(input())
# l = list(map(int,input().split(' ')))
# keys = sorted(set(l))
# max = 0
# result = 0
# for i in keys:
#     if l.count(i) > max:
#         result = i
#         max = l.count(i)
# print(result)

# 2013-12-02  IBSN号码
'''
0-670-82162-4
最后一位为识别码。
识别码的计算方法如下：
　　首位数字乘以1加上次位数字乘以2……以此类推，用所得的结果mod 11，所得的余数即为识别码，如果余数为10，则识别码为大写字母X。例如ISBN号码0-670-82162-4中的识别码4是这样得到的：对067082162这9个数字，从左至右，分别乘以1，2，…，9，再求和，即0×1+6×2+……+2×9=158，然后取158 mod 11的结果4作为识别码。
　　编写程序判断输入的ISBN号码中识别码是否正确，如果正确，则仅输出“Right”；如果错误，则输出是正确的ISBN号码。
'''

# l = input()
# x = l[-1]
# new_l = l.replace('-', '')
# new_l = new_l[:-1]
# result = 0
#
# for i in range(len(new_l)):
#     result += (i + 1) * int(new_l[i])
#
# result = result % 11
# if result == 10:
#     if x == 'X':
#         print('Right')
#     else:
#         print(l[:-1] + 'X')
# else:
#     if str(result) == x:
#         print('Right')
#     else:
#         print(l[:-1] + str(result))

#2013-12-3
'''
解题思路：
以当前高度为标准，分别向左和向右两个方向检查，如果高度大于等于当前高度width+1,否则停止继续扫描
计算当前最大面积大小size，如果大于maxSize，更新max
'''
# n = int(input())
# l = list(map(int,input().split(' ')))
# maxSize = 0
# for i in range(n):
#     width = 1
#     for j in range(i+1,n): #向右检查
#         if l[j]>=l[i]:
#             width += 1
#         else:
#             break
#     for j in range(i-1,-1,-1): #向左检查
#         if l[j]>=l[i]:
#             width += 1
#         else:
#             break
#     size = width * l[i]
#     if size > maxSize:
#         maxSize = size
# print(maxSize)

#2013-12-04  有趣的数
def judgeQ(n):
    if n[0] == '0':
        return False
    if n.replace('0', '').replace('1', '').replace('2', '').replace('3','') == '':
        if n.count('0') >= 1 and n.count('1') >= 1 and n.count('2') >= 1 and n.count('3') >= 1:
            pass
        else:
            return False
    else:
        return False
    l0 = []
    l1 = []
    l2 = []
    l3 = []
    for i in range(len(n)):
        if n[i] == '0':
            l0.append(i)
        elif n[i] == '1':
            l1.append(i)
        elif n[i] == '2':
            l2.append(i)
        elif n[i] == '3':
            l3.append(i)
    if l0[len(l0)-1] < l1[len(l1)-1]:
        pass
    else:
        return False
    if l2[len(l2)-1] < l3[len(l3)-1]:
        return True
    else:
        return False


n = int(input())
count = 0
print(count%1000000007)