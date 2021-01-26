# A1041
from collections import defaultdict


def unique():
    l = input().split(' ')
    l = list(map(int, l))
    l.pop(0)
    d = defaultdict(list)
    for i in range(len(l)):
        d[l[i]].append(1)
    result = ''
    for key in d.keys():
        if len(d[key]) == 1:
            result = key
            break
    if result == '':
        print("None")
    else:
        print(result)


# A1050
'''
学到 如果用下标获取也会花费一些时间 可以直接取不通过下标
'''


def stringSub():
    l1 = input()
    l2 = input()
    for i in l2:
        l1 = l1.replace(i, '')
    print(l1)


# B1005
'''
n%2 == 0 n = n/2
n%2 != 0 n = (3*n+1)/2
采用hashtable想法做 但是占用的内存太大了
又借鉴了大神的代码
'''
import copy


def nn():
    k = int(input())
    l = input().split(' ')
    l = list(map(int, l))
    l = sorted(l, reverse=True)

    hashTable = [i * 0 for i in range(9999)]
    for i in range(len(l)):
        x = copy.copy(l[i])
        while x != 1:
            if (x % 2 == 0):
                x = int(x / 2)
                hashTable[x] += 1
            else:
                x = int((3 * x + 1) / 2)
                hashTable[x] += 1
    result = ''
    for i in range(len(l)):
        if hashTable[l[i]] == 0:
            if (result == ''):
                result = str(l[i])
            else:
                result = result + ' ' + str(l[i])
    print(result)


def nn2():
    input_number = int(input())

    # 记录每个数字计算的过程
    def record_3n(calculate_number):
        record_list = []
        while True:
            if calculate_number == 1:
                break
            # 3n+1思想
            calculate_number = calculate_number // 2 if calculate_number % 2 == 0 else (calculate_number * 3 + 1) // 2
            record_list.append(calculate_number)
        # 去除计算中出现的重复元素
        return set(record_list)

    input_list = input().split()
    # 输入字符串转换成整数类型
    each_number = set([int(number) for number in input_list])

    while input_number:
        for number in input_list:
            # 记录每个数字的3n+1计算出现的数字
            record_result = record_3n(int(number))
            # 记录不在record_3n中的结果
            each_number = each_number.difference(record_result)
            input_number -= 1

    result = list(each_number)
    # 由大到小排序
    result.sort(reverse=True)
    result = [str(i) for i in result]
    print(' '.join(result))


# A1048
'''
运行超时
findCoin3没有超时
'''


def findCoin():
    l1 = input().split(' ')
    n = int(l1[0])  # n个硬币
    m = int(l1[1])  # 需要付的钱
    l2 = input().split(' ')  # n个硬币的面值
    l2 = sorted(list(map(int, l2)))
    tag = 0
    for i in range(len(l2)):
        if (m - l2[i] in l2):
            if (m - l2[i] == l2[i] and l2[i] != l2[i + 1]):
                pass
            else:
                print(l2[i], m - l2[i])
                tag = 1
                break
    if tag == 0:
        print("No Solution")


def findCoin2():
    l = input().split(' ')
    n, m = int(l[0]), int(l[1])
    l = input().split(' ')
    l = list(map(int, l))
    d = [0 for x in range(1000)]
    for x in l:
        d[x] += 1
    for x in range(1000):
        if d[x] > 0:
            temp = m - x
            if temp != x:
                if d[temp] > 0:
                    print(x, temp)
                    return
            else:
                if d[temp] > 1:
                    print(x, temp)
                    return
    print("No Solution")


def findCoin3():
    l = input().split(' ')
    n, m = int(l[0]), int(l[1])
    l = input().split(' ')
    l = list(map(int, l))
    d = [0 for x in range(1000)]
    for x in l:
        d[x] += 1
    l = sorted(l)
    for i in l:
        if (d[i] > 0):
            x = m - i
            if x == i and d[x] > 1:
                print(i, x)
                return
            elif x != i and d[x] > 0:
                print(i, x)
                return
    print("No Solution")


if __name__ == '__main__':
    # nn()
    # nn2()
    # unique()
    # stringSub()
    # findCoin()
    # findCoin2()
    findCoin3()
