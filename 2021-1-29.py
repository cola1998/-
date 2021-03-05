#最大公约数 codeup 1818
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

# def GCD():


# 最小公倍数
def lcm(a,b):
    # 注意前提是a >= b，若a < b需要互换位置
    d = gcd(a,b)
    return a/d*b

#codeup100000589
def LCM():
    n = int(input())
    ll = []
    for i in range(n):
        l = list(map(int, input().split(' ')))
        l.pop(0)
        ll.append(l)
    for l in ll:
        for i in range(len(l)-1):
            l[i+1] = lcm(l[i],l[i+1])
        print(int(l[len(l)-1]))

#B1008
def youYi():
    n = input().split(' ')
    m = int(n[1])
    n = int(n[0])
    l = list(map(int, input().split(' ')))
    m = m%n #修正m
    if m != 0:
        d = gcd(m,n)
        print(d)
        for i in range(n-m,n-m+d):
            temp = l[i]
            pos = i
            while True:
                next = (pos-m+n)%n
                if next!=i:
                    #如果下一个位置不是初始点，把下一个位置的元素赋值给当前处理的位置
                    l[pos] = l[next]
                else:
                    #否则把一开始拿走的元素赋值给最后这个空位
                    l[pos] = temp
                pos = next #传递位置
                if pos == i:
                    break

        for i in range(n):
            if i==n-1:
                print(l[i])
            else:
                print(l[i],end=' ')

#判断素数
import math
def isPrime(n):
    if n<=1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3,int(math.sqrt(n)+1),2):
        if n%i == 0:
            return False
    return True

#输出100以内的素数
def findPrime():
    primeList = []
    for i in range(101):
        if isPrime(i):
            primeList.append(True)
            if i!=100:
                print(i,end=' ')
            else:
                print(i)
        else:
            primeList.append(False)

#B1013数素数
def countPrime():
    l = list(map(int,input().split(' ')))
    for i in range(l[0],l[1]+1):
        if isPrime(i):
            print(i)
        else:
            pass

if __name__ == "__main__":
    # LCM()
    # youYi()
    # findPrime()
    findPrime()