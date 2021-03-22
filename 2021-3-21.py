#202009-1
# n,X,Y = map(int,input().split())
# position = []
# for i in range(n):
#     xi,yi = map(int,input().split())
#     dis = pow(X-xi,2) + pow(Y-yi,2)
#     position.append([xi,yi,dis,i+1])
# position = sorted(position,key=lambda x:x[2],reverse=False)
# for i in range(3):
#     print(position[i][3])

#202009-2
# def judge(xl,yd,xr,yu,x,y):
#     if x>=xl and x<=xr and y<=yu and y>=yd:
#         return True
#     else:
#         return False
# n,k,t,xl,yd,xr,yu = map(int,input().split())
# position = []
# count_t = 0 #曾经经过高危区人数
# count_d = 0 #曾在高危区逗留
# for i in range(n):
#     l = list(map(int,input().split()))
#     tag = 0
#     count = 0
#     for j in range(0,len(l),2):
#         if judge(xl,yd,xr,yu,l[j],l[j+1]):
#             tag = 1
#             count += 1
#             if count >= k:
#                 count_d += 1
#                 break
#         else:
#             count = 0
#
#     if tag == 1:
#         count_t += 1
# print(count_t)
# print(count_d)