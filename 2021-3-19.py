#201912-1
# n = int(input())
# p = [0*i for i in range(4)]
# i = 0 #记录当前报数人id
# num = 0 #记录当前报数的数字
# while n > 0:
#     num += 1
#     if num%7==0 or '7' in str(num):
#         p[i] += 1
#     else:
#         n -= 1
#         if n == 0:
#             break
#     i += 1
#     i = i % 4
# for j in range(4):
#     print(p[j])

#201912-2
# n = int(input())
# location = []
# num = [0 for i in range(5)]
# x = [1,-1,1,-1]
# y = [1,1,-1,-1]
# for i in range(n):
#     xi,yi = map(int,input().split())
#     location.append([xi,yi])
# for i in range(n):
#     xi,yi = location[i][0],location[i][1]
#     if [xi-1,yi] in location and [xi+1,yi] in location and [xi,yi-1] in location and [xi,yi+1] in location:
#         #该点适合做回收站
#         count = 0
#         for j in range(4):
#             if [xi+x[j],yi+y[j]] in location:
#                 count += 1
#         num[count] += 1
# for i in range(5):
#     print(num[i])


'''
测试样例:
7
1 2
2 1
0 0
1 1
1 0
2 0
0 1
'''