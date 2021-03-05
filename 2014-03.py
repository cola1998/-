#01相反数
# n = int(input())
# l = sorted(list(map(int,input().split(' '))))
# count = 0
# for i in range(len(l)):
#     if l[i] > 0:
#         break
#     if l[i] < 0 and (-l[i] in l):
#         count += 1
# print(count)

#02 窗口
# def judgeW(point,win):
#     for i in range(len(win)):
#
#
# n,m = map(int,input().split(' '))
# win = []  # 存储窗口位置
# order = []   # 窗口顺序
# for i in range(n):
#     win.append(input().split(' '))
#     order.append(i+1)
# point = []
# for i in range(m):
#     point.append(input().split(' '))
#
# result = []
# "IGNORED"

#201409-1  相对数对
# n = int(input())
# l = list(map(int,input().split()))
# l.sort()
# count = 0
# for i in range(len(l)-1):
#     if l[i+1]-l[i] == 1:
#         count += 1
# print(count)

#201409-02
'''
思路：得到每一个区域(x1,y1) (x2,y2),遍历整个区域，将每一个方格左下顶点加入cellss
使用set数据结构自动去重，最后输出cells长度即为面积大小
'''
# n = int(input())
# l = []
# cells = set()
# for i in range(n):
#     x1,y1,x2,y2 = map(int,input().split())
#     x_step = 1 if x1<=x2 else -1
#     y_step = 1 if y1<=y2 else -1
#     for x in range(x1,x2,x_step):
#         for y in range(y1,y2,y_step):
#             cells.add((x,y))
# print(len(cells))



