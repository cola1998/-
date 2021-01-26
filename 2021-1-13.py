# 递归求解n的阶乘
def f(n):
    if n == 0:
        return 1
    else:
        return f(n - 1) * n


# 递归求解斐波那楔数列
def ff(n):
    if n == 0 or n == 1:  # 递归边界
        return 1
    else:  # 递归式
        return ff(n - 1) + ff(n - 2)
# 全排列
def generateP(index):
    if index == n+1:
        for i in p:
            print(i,end=' ')
        print('')
        return


if __name__ == '__main__':
    x = f(3)
    print(x)
    x = ff(4)
    print(x)

    n = 3
    hashTable = [0 for x in range(n)]
    p = []