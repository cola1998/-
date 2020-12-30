import math
x_list = input().split(' ')
y_list = input().split(' ')

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0


for i in range(len(x_list)):
    x_list[i] = float(x_list[i])
    y_list[i] = float(y_list[i])
    sum1 += math.pow(math.sin(x_list[i]),2)
    sum2 += math.pow(math.cos(x_list[i]),2)
    sum3 += math.sin(x_list[i])*y_list[i]
    sum4 += math.cos(x_list[i])*y_list[i]
    sum5 += math.sin(x_list[i])*math.cos(x_list[i])

print("sum1=",sum1)
print("sum2=",sum2)
print("sum3=",sum3)
print("sum4=",sum4)
print("sum5=",sum5)

