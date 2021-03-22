# #202006-1
n,m = map(int,input().split())
info = [] #{x:*,y:*,tag:*}
a_list = []
b_list = []
for i in range(n):
    d = {}
    x,y,tag = input().split()
    if tag == 'A':
        a_list.append([int(x),int(y)])
    else:
        b_list.append([int(x),int(y)])
a_list = sorted(a_list)
b_list = sorted(b_list)
query = []
for i in range(m):
    query.append(list(map(int,input().split())))
for i in range(m):
    d0,x0,y0 = query[i]
    a_tag = []
    b_tag = []
    for p in a_list:
        if d0 + p[0]*x0 +p[1]*y0 < 0:
            a_tag.append(p)
        else:
            b_tag.append(p)
    for p in b_list:
        if d0 + p[0]*x0 +p[1]*y0 < 0:
            a_tag.append(p)
        else:
            b_tag.append(p)
    a_tag = sorted(a_tag)
    b_tag = sorted(b_tag)
    if a_tag == a_list and b_tag == b_list:
        print('Yes')
    else:
        print('No')

#202006-2
# n,a,b =  map(int,input().split())
# u = {}
# v = {}
#
# for i in range(a):
#     l,x = map(int,input().split())
#     u[l-1] = x
# for i in range(b):
#     l,x = map(int,input().split())
#     v[l-1] = x
# sum = 0
#
# for k in u.keys():
#     if k in v:
#         sum += u[k]*v[k]
# print(sum)