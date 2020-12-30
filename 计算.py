import math
x_list = input().split(' ')
y_list = input().split(' ')

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sumy = 0
sumxy = 0
sum2y = 0
sum3y = 0
for i in range(len(x_list)):
    x_list[i] = float(x_list[i])
    y_list[i] = float(y_list[i])
    sum1 += x_list[i]
    sum2 += math.pow(x_list[i],2)
    sum3 += math.pow(x_list[i],3)
    sum4 += math.pow(x_list[i],4)
    sum5 += math.pow(x_list[i], 5)
    sumy += y_list[i]
    sumxy += (x_list[i]*y_list[i])
    sum2y += (math.pow(x_list[i],2)*y_list[i])
    sum3y += (math.pow(x_list[i],3)*y_list[i])

print("sum1=",sum1)
print("sum2=",sum2)
print("sum3=",sum3)
print("sum4=",sum4)
print("sum5=",sum5)
print("sumy=",sumy)
print("sumxy=",sumxy)
print("sum2y=",sum2y)
print("sum3y=",sum3y)
