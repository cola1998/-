#201903-1
'''
注意：中位数的计算：整数要输出整数 小数要四舍五入保留一位
'''
# n = int(input())
# l = list(map(int,input().split()))
# l = sorted(l)
# if n%2==0:
#     mid = (l[int(n/2)] + l[int(n/2)-1])/2
#     if mid%1==0.0:
#         mid = int(mid)
#     else:
#         mid = round(mid,1)
# else:
#     mid = l[int(n/2)]
# print("{0} {1} {2}".format(l[n-1],mid,l[0]))

#201903-2 二十四点
'''
注意：是x不是*
'''
def yxj(s):
    if s == '-' :
        return 1
    elif s == '+':
        return 1
    elif s == 'x':
        return 2
    else:
        return 2
def jisuan(x1,x2,s):
    if s == '-' :
        return x1-x2
    elif s == '+':
        return x1+x2
    elif s == 'x':
        return x1*x2
    elif s=='/' and x2!=0:
        return x1//x2
#模拟栈实现
n = int(input())
l = []
result = []
for i in range(n):
    s = input()
    s = list(s)
    cs = [] #当做栈用 操作数栈
    fs = [] #操作符栈
    for j in range(len(s)):
        if j % 2 == 0:
            cs.append(int(s[j]))
            continue
        if len(fs)==0 or yxj(fs[-1])<yxj(s[j]):
            fs.append(s[j])
        elif yxj(fs[-1]) == yxj(s[j]): #等于先不入栈
            x1 = cs.pop()
            x2 = cs.pop()
            f = fs.pop()
            cs.append(jisuan(x2,x1,f))
            fs.append(s[j])
        else:
            while yxj(fs[-1])>yxj(s[j]):
                x1 = cs.pop()
                x2 = cs.pop()
                f = fs.pop()
                cs.append(jisuan(x2, x1, f))
                if len(fs) == 0:
                    break
            fs.append(s[j])
    while len(fs) != 0:
        x1 = cs.pop()
        x2 = cs.pop()
        f = fs.pop()
        cs.append(jisuan(x2, x1, f))
    if len(cs) == 1 and int(cs[0]) == 24:
        print('Yes')
    else:
        print('No')

#大神版
'''
注意事项：整除 应该用//
'''
# n=int(input())
# for i in range(n):
#     s=input()
#     s=s.replace('x','*')
#     s=s.replace('/','//')
#     s=eval(s)
#     if s==24:
#         print('Yes')
#     else:
#         print('No')