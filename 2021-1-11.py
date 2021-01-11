#B1039  自己写的测试点两个无法通过
def change(s):
    if(s>='0' and s<='9'):
        return int(s)
    elif s>'a' and s<'z':
        return ord(s)-87
    elif s>'A' and s<'Z':
        return ord(s)-55
    else:
        return -1
def buy():
    l1 = input() #摊主给出的珠串
    l2 = input() #小红想做的珠串
    hashTable = [i*0 for i in range(62)]
    for i in range(len(l1)):
        x = change(l1[i])
        if(x != -1):
            hashTable[x] += 1
    miss = 0
    for i in range(len(l2)):
        x = change(l2[i])
        if(x != -1):
            hashTable[x] -= 1
            if hashTable[x]<0:
                miss += 1
    if miss>0:
        print('No {}'.format(miss))
    else:
        result = sum(hashTable)
        print('Yes {}'.format(result))
'''
只能借鉴一下大神的代码
'''
def buyOrNot():
    s1=input()
    s2=input()
    s2_set=set(list(s2))
    print(s2_set)
    shao=0
    for i in s2_set:
        cha=s2.count(i)-s1.count(i)
        if(cha>0):
            shao+=cha
    if(shao!=0):
        print("No",shao)
    else:
        print("Yes",len(s1)-len(s2))

#B1042
# def countString():
#     l = input().lower()
#     l = list()
#     l_set = set(l)
#     sorted(l_set)
#     max = 0
#     k = ''
#     for x in l_set:
#         if(l.count(x)>max and x>='a' and x<='z'):
#             max = l.count(x)
#             k = x
#     print(k,max)
'''
又是借鉴大神代码的一天
'''
def StringCount():
    s = input().lower()
    res = []
    for i in range(97,123):
        res.append(s.count(chr(i)))

    print(chr(res.index(max(res))+97),max(res))

#B1043
def printPAT():
    l = input()
    x = 'PATest'
    num = []
    sum = 0
    for i in range(len(x)):
        sum += l.count(x[i])
        num.append(l.count(x[i]))
    m = min(num)
    result = ''
    for i in range(m):
        result = result + 'PATest'
    sum -= (m*len(x))
    for i in range(len(num)):
        num[i] -= m
        if(num[i])>0:
            num[i] -= 1
            result = result + x[i]
            sum -= 1
    while sum > 0:
        for i in range(len(num)):
            if (num[i]) > 0:
                num[i] -= 1
                result = result + x[i]
                sum -= 1
    print(result)

#B1047
from collections import defaultdict
def ProgramContest():
    n = int(input())
    inf = defaultdict(list)
    for i in range(n):
        l_r = input().split(' ')
        l = list(l_r[0].split('-'))
        inf[l[0]].append(int(l_r[1]))
    keys = []
    for key in inf.keys():
        keys.append(key)
    max = 0
    k = 0
    for key in keys:
        if sum(inf[key])>max:
            max = sum(inf[key])
            k = key
    print('{0} {1}'.format(k,max))
if __name__ == '__main__':
    # buy()
    # buyOrNot()
    # countString()
    # StringCount()
    # printPAT()
    ProgramContest()