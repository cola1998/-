#201612-1  中间数
# n = int(input())
# l = sorted(list(map(int,input().split())))
#
# flag = 0
# if n%2 == 0:
#     #检查两边数是否相等，不相等
#     mid = int(n/2)-1
#     if l[mid] != l[mid+1]:
#         print(-1)
#         flag = -1
# else:
#     mid = int(n/2)
#
# if flag == 0:
#     minn = 0
#     maxn = 0
#     for i in range(n):
#         if l[i] < l[mid]:
#             minn += 1
#         elif l[i] > l[mid]:
#             maxn += 1
#     if maxn == minn:
#         print(l[mid])
#     else:
#         print(-1)

#201612-2 工资计算
'''
思路 计算出税后的区间
x = 3500 + 1500 - 1500*0.1
x = x + (4500-1500) - (4500-1500) * 0.2
....
注意最后除以(1-3%) 不要弄错
'''
# T = int(input())  #税后工资
# if T <= 3500:
#     print(T)
# elif T <= 4955:
#     print(int((T - 3500)/(1-0.03) + 3500))
# elif T <= 7655:
#     print(int((T-4955)/(1-0.1)+5000))
# elif T <= 11255:
#     print(int((T-7655)/(1-0.2)+8000))
# elif T <= 30755:
#     print(int((T-11255)/(1-0.25)+12500))
# elif T <= 44755:
#     print(int((T-30755)/(1-0.3)+38500))
# elif T <= 61005:
#     print(int((T-44755)/(1-0.35)+58500))
# else:
#     print(int((T-61005)/(1-0.45)+83500))

#201612-3   90分？？？
p = int(input())
category = {}
for i in range(p):
    x = input()
    if ':' in x:
        x = x.split(':')
        category[x[0]] = int(x[1])
    else:
        category[x] = -1  #代表该权限不分等级

r = int(input())
role = {} #角色
for i in range(r):
    x = input().split()
    p = {}
    for j in x[2:2+int(x[1])]:
        if ':' in j:
            j = j.split(':')
            p[j[0]] = int(j[1])
        else:
            p[j] = -1
    role[x[0]] = p

u = int(input())
user = {} #用户
for i in range(u):
    x = input().split()
    ll = x[2:2+int(x[1])]
    pp = {}
    for r in ll:
        for key in role[r].keys():
            if key not in pp:
                pp[key] = role[r][key]
            else:
                pp[key] = max(role[r][key],pp[key])
    user[x[0]] = pp
q = int(input())
result = []  #查询 用户是否具有这样的权限
lq = []
for i in range(q):
    x = input().split()
    lq.append(x)
for x in lq:
    username = x[0]
    if ':' in x[1]:
        s = x[1].split(':')
        privilege = s[0]
        if s[1] != "":
            number = int(s[1])
        else:
            number = -1
    else:
        privilege = x[1]
        number = -1
    if username in user:
        if privilege in user[username]:
            if number == -1:
                if user[username][privilege] == -1:#无等级查询
                    result.append('true')
                else: #查询等级
                    result.append(user[username][privilege])
            else:
                if user[username][privilege] >= number:#验证等级
                    result.append('true')
                else:
                    result.append('false')
        else:#不具有该privilege
            result.append('false')
    else:#系统中不存在这个用户
        result.append('false')

for i in result:
    print(i)