#3.6字符串处理
#codeup 5901 回文串
# l = input()
# tag = 0
# for i in range(int(len(l)/2)):
#     if(l[i]!=l[len(l)-1-i]):
#         tag = -1
#         break
# if(tag==-1):
#     print('NO')
# else:
#     print('YES')
#B1009
#注意是单词顺序调换
l = input().split(' ')
result = ''
for i in range(len(l)-1,-1,-1):
    if result=='':
        result = result+l[i]
    else:
        result = result+' '+l[i]
print(result)