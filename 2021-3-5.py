# 201503-1
# n,m = map(int,input().split())
# martix = []
# for i in range(n):
#     l = list(map(int,input().split()))
#     martix.append(l)
# for i in range(m-1,-1,-1):
#     for j in range(n):
#         print(martix[j][i],end='')
#         if j == n-1:
#             print()
#         else:
#             print('',end=' ')

# 201503-2
# n = int(input())
# l = list(map(int, input().split()))
# d = {}
# for i in range(len(l)):
#     if l[i] not in d.keys():
#         d[l[i]] = 1
#     else:
#         d[l[i]] += 1
# d = sorted(d.items(), key=lambda item: (item[1],-item[0]), reverse=True)
# for i in d:
#     print("{0} {1}".format(i[0], i[1]))

# 201503-3
def isRun(year):
    if year % 400 == 0:
        return 1
    elif year % 4 == 0 and year % 100 != 0:
        return 1
    else:
        return 0

def get_day(year,month):
    d = 0  # 该月1号与1850年1月1日差多少天
    #计算之前年份的天数
    d += (year-1850)*365
    for i in range(1850,year):
        if isRun(i)==1:
            d+=1

    #计算当年的天数
    for i in range(month):
        d += days[i]
    if isRun(year) == 1 and month > 2:
        d += 1
    week = (d%7 + 2)%7  #0是星期日 1是星期一
    return week,d


days = [31,28,31,30,31,30,31,31,30,31,30,31]
a,b,c,y1,y2 = map(int,input().split())
for x in range(y1,y2+1,1):
    result = "{0}/{1}/".format(x,a)
    week0,day0 = get_day(x,a)
    if week0 == 0:
        week0 = 7
    day = 0 #记录这个月的天数 作为判断条件避免超出
    print("{0}年{1}月的1号星期{2} {3}天".format(x,a,week0,day0))
    if week0 > c:
        day += 7 - week0 + 1
        day += (b-1)*7+c
        print(day)
    elif week0 <= c:
        day += (b - 1) * 7 + c
        day -= (week0+1)
        print(day)
    elif week0 == 1:
        day += (b-1)*7 +c
        print(day)
