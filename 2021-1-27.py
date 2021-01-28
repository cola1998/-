def quicksort(arr, low, high):
    left = low
    right = high
    k = arr[low]
    if (left >= right):
        return
    while (left < right):
        while (left < right and arr[right] >= k):
            right -= 1
        arr[left] = arr[right]
        while (left < right and arr[left] <= k):
            left += 1
        arr[right] = arr[left]
    arr[left] = k
    quicksort(arr, low, left - 1)
    quicksort(arr, left + 1, high)
    return arr


# 5.1 简单数学 B1003
def checkString(s):
    if s.replace('P', '').replace('A', '').replace('T', '') != '':
        return False
    if s.count('P') != 1:
        return False
    if s.count('T') != 1:
        return False
    if s.index('P') > s.index('T'):
        return False
    p = s.index('P')
    t = s.index('T')
    n1 = p
    n2 = t - p - 1
    n3 = len(s) - 1 - t
    if n2 == 0:
        return False
    if n1 * n2 == n3:
        return True
    else:
        return False


def WantPass():
    n = int(input())
    for i in range(n):
        x = input()
        if checkString(x) == True:
            print('YES')
        else:
            print('NO')


# B1019
'''
1、string如何在左边填充字符rjust(4,'0')
2、测试样例2,3,4分别是输入数字一位两位三位
'''


def newNumber(s):
    l = []
    s = s.rjust(4, '0')
    for i in range(len(s)):
        l.append(int(s[i]))
    l = sorted(l)
    min = ''.join([str(x) for x in l])
    l = sorted(l, reverse=True)
    max = ''.join([str(x) for x in l])
    return int(max), int(min)


def BlackHole():
    n = input()
    i = 1
    flag = 0
    for i in range(1, len(n)):
        if n[i] != n[i - 1]:
            flag = 1
            break
    if flag != 1 and len(n) >= 2:
        print("{0} - {1} = 0000".format(n, n))
        return

    while True:
        max, min = newNumber(n)
        n = str(max - min)
        if n == '6174':
            print("{0} - {1} = {2}".format(str(max).rjust(4, '0'), str(min).rjust(4, '0'), n.rjust(4, '0')))
            break
        else:
            print("{0} - {1} = {2}".format(str(max).rjust(4, '0'), str(min).rjust(4, '0'), n.rjust(4, '0')))


# B1049
'''
1、规律 每个数字出现i*(n-i+1) 直接求和即可
2、不能使用float 精度不够，应该使用Decimal
'''
from decimal import Decimal


def partHe():
    n = int(input())
    sum = Decimal(0)
    l = list(map(Decimal, input().split(' ')))
    for i in range(n):
        sum += (i + 1) * (n - i) * l[i]
    print(sum.quantize(Decimal('0.00')))


# A1008
def Elevator():
    l = list(map(int, input().split(' ')))
    n = l[0]
    l.pop(0)
    total = 0
    now = 0  # 表示当前楼层
    for i in range(len(l)):
        if l[i] > now:
            total += 6 * (l[i] - now)
        elif l[i] < now:
            total += 4 * (now - l[i])
        total += 5
        now = l[i]
    print(total)


# A1049
def countOne():
    n = input()
    count = 0
    a = 1
    for i in range(len(n)):
        index = len(n) - i - 1
        now = int(n[index])
        if now == 0:
            left = int(n[:index]) if n[:index] != '' else 0
            count += left * a
        elif now == 1:
            left = int(n[:index]) if n[:index] != '' else 0
            right = int(n[index + 1:]) if n[index + 1:] != '' else 0
            count += left * a + right + 1
        else:
            left = int(n[:index]) if n[:index] != '' else 0
            count += (left + 1) * a
        a *= 10
    print(count)

#B1008 最大公约数和最小公倍数

def youYi():
    n = input().split(' ')
    m = int(n[1])
    l = list(map(int,input().split(' ')))



if __name__ == '__main__':
    # l = [8, 7, 12, 1, 5, 0, 6, 9, 2]
    # s = quicksort(l, 0, len(l)-1)
    # print(s)
    # WantPass()
    # BlackHole()
    # partHe()
    # Elevator()
    countOne()