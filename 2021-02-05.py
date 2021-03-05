from math import sqrt
def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3,int(sqrt(n)+1),2):
        if n%i == 0:
            return False
    return True

def findPrime(x):
    primeList = []
    for i in range(x+1):
        if isPrime(i):
            primeList.append(True)
        else:
            primeList.append(False)
'''
质因子分解
'''

