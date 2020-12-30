#A1002
#求两个多项式的和
l1 = input().split(' ')
l2 = input().split(' ')
i = 1
j = 1
max_n = max(int(l1[1]),int(l2[1]))
result_list = [i*0 for i in range(max_n)]

for i in range(1,len(l1),2):
    while int(l2[j]) > int(l1[i]):
        result_list.append(float(l2[j+1]))
        j += 2
    if int(l2[j]) == int(l1[j]):
        result_list.append(float(l2[j+1]) + float(l2[i+1]))
for i in range(len(result_list)):
    if result_list[i] != 0:
        if i == len(result_list)-1:
            print('{0} {1}'.format(i,result_list[i]))
        else:
            print('{0} {1}'.format(i, result_list[i]), end=' ')
#A1009
#求两个多项式的乘积
# l1 = input().split(' ')
# l2 = input().split(' ')
# i = 1
# j = 1
# result_list = []
# for i in range(1,len(l1),2):
