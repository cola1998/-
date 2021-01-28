# B1023
def zuxiaoshu():
    l = input().split(' ')
    l = list(map(int, l))
    result = ''
    for i in range(1, len(l)):
        if (l[i] != 0):
            result = str(i) + result
            l[i] -= 1
            break

    for i in range(len(l)):
        if (l[i] != 0):
            for j in range(l[i]):
                result = result + str(i)
    print(result)


# B1020
def moonCake():
    l = input().split(' ')
    n = int(l[0])
    d = float(l[1])
    l = input().split(' ')
    k = list(map(float, l))  # 每种的库存量
    l = input().split(' ')
    price = list(map(float, l))  # 每种的总售价

    per_prince = {}
    for i in range(n):
        per_prince[i] = price[i] / k[i]
    per_prince = sorted(per_prince.items(), key=lambda x: x[1], reverse=True)
    profit = 0
    for item in per_prince:
        item = list(item)
        if d >= k[item[0]]:
            profit += price[item[0]]
            d -= k[item[0]]
        else:
            profit += (item[1] * d)
            d = 0
            break
    print('{:.2f}'.format(profit))


# A1033
def choose_fill(now, d, Cmax, D, Davg):
    '''
    遍历每一个dict 筛选出当前可以到达的所有加油站
    :param now: 当前点
    :param d: list
    :return:
    '''
    minPrice = d[now]['price']
    minDistance = 0
    flag = 0
    for i in d:
        if i['dis'] <= d[now]['dis'] + float(Cmax / Davg):
            flag = 2
            if i['price'] < minPrice:
                minPrice = i['price']
                minDistance = i['dis']
                flag = 1
                return minPrice, minDistance
    if flag == 0:
        # 表示一直没有进入内层循环,没有可以到达的加油站了
        return 0


def fill_test():
    l = input().split(' ')
    Cmax = float(l[0])  # 油箱中最大容量
    D = float(l[1])  # 起点到终点的距离
    Davg = float(l[2])  # 单位汽油能够支持前进davg

    N = int(l[3])
    d = []
    for i in range(N):  # 给定的N个加油站的单位油价和离起点的距离
        l = input().split(" ")
        d.append({'price': float(l[0]), 'dis': float(l[1])})
    d.append({'price': 0, 'dis': D})
    # 第一步把所有加油站按照距离由小到大排序
    d = sorted(d, key=lambda x: x['dis'])

    if d[0]['dis'] != '0':
        print("The maximum travel distance=0.00")
        return
    price = d[0]['price'] * Cmax
    contain = 0
    now = 0
    while (True):
        if now == D:
            print('The maximum travel distance={:.2f}'.format(price))
            return
        temp = sorted([x for x in d if x['dis'] > d[now]['dis'] and x['dis'] <= d[now]['dis'] + float(Cmax / Davg)],
                      key=lambda t: t['price'])
        if len(temp) > 0:
            arr = [t for t in temp if t['price'] < d[now]['price']]
            if len(arr) == 0:
                # 选择第一个即可
                contain = Cmax - (temp[0]['dis'] - now) / Davg
                price += temp[0]['price'] * contain
                now = temp[0]['dis']
            else:
                contain = Cmax - (arr[0]['dis'] - now) / Davg
                price += arr[0]['price'] * contain
                now = arr[0]['dis']
        else:
            print('The maximum travel distance={:.2f}'.format(price))
            return


# A1037
def magicCoupon():
    n1 = int(input())
    l1 = list(map(int, input().split(' ')))
    n2 = int(input())
    l2 = list(map(int, input().split(' ')))

    sum = 0
    l1 = sorted(l1)
    l2 = sorted(l2)
    for i in range(len(l1)):
        if l1[i] < 0 and l2[i] < 0:
            sum += l1[i] * l2[i]
        else:
            break
    i = len(l1) - 1
    j = len(l2) - 1
    while (i >= 0 and j >= 0 and l1[i] > 0 and l2[j] > 0):
        sum += l1[i] * l2[j]
        i -= 1
        j -= 1
    print(sum)


# A1067
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


def sortWithSwap():
    n = int(input())
    l = list(map(int, input().split(' ')))
    times = 0
    k = 0  # 记录不在本位的数字个数
    pos = [0 for i in range(len(l))]
    for i in range(len(l)):
        if i != l[i] and i != 0:
            k += 1
        pos[l[i]] = i

    while k > 0:
        # 如果0在本位上
        if pos[0] == 0:
            for i in range(len(pos)):
                if pos[i] != i:
                    pos[0], pos[i] = swap(pos[0], pos[i])
                    times += 1
                    break
        while pos[0] != 0:
            s = pos[0]
            pos[0], pos[s] = swap(pos[0], pos[pos[0]])
            k -= 1
            times += 1
    print(times)


# A1038
def buble_sort():
    l = [8, 7, 12, 1, 5, 0, 6, 9, 2]
    for i in range(len(l) - 1):
        for j in range(len(l) - i - 1):
            if(l[j] < l[j + 1]):
                l[j],l[j + 1] = swap(l[j], l[j + 1])
    print(l)
if __name__ == "__main__":
        # zuxiaoshu()
        # moonCake()
        # fill_test()
        # magicCoupon()
        # sortWithSwap()
    buble_sort()