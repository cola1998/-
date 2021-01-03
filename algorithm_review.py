#Horspool算法
def shiftTable(P):
    m = len(P)
    Table = {}
    for i in range(m):
        Table[P[i]] = m-i
    return Table
def Horspool(T,P):
    table = shiftTable(P)
    i = 0
    m = len(P)
    n = len(T)
    while i<n:
        k = 0
        while k<m and T[i-k]==P[m-k-1]:
            k+=1
        if(k==m):
            return i-m+1
        else:
            print(T[i],table.get(T[i],6))
            i = i+table.get(T[i],6)
    return -1
P = ['B','A','R','B','E','R']
T = ['J','I','M','_','_','S','A','W','_','M','E','_','I','_','A','_','B','A','R','B','E','R','S','H','O','P']
table = shiftTable(P)
print(table)
k = Horspool(T,P)
print(k)