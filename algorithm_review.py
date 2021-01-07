#Horspool算法
# def shiftTable(P):
#     m = len(P)
#     Table = {}
#     for i in range(m):
#         Table[P[i]] = m-i
#     return Table
# def Horspool(T,P):
#     table = shiftTable(P)
#     i = 0
#     m = len(P)
#     n = len(T)
#     while i<n:
#         k = 0
#         while k<m and T[i-k]==P[m-k-1]:
#             k+=1
#         if(k==m):
#             return i-m+1
#         else:
#             print(T[i],table.get(T[i],6))
#             i = i+table.get(T[i],6)
#     return -1
# P = ['B','A','R','B','E','R']
# T = ['J','I','M','_','_','S','A','W','_','M','E','_','I','_','A','_','B','A','R','B','E','R','S','H','O','P']
# table = shiftTable(P)
# print(table)
# k = Horspool(T,P)
# print(k)

#快速排序
def swap(A,i,j):
    temp = A[j]
    A[j] = A[i]
    A[i] = temp

def Partition(A,l,r):
    i = l+1
    j = r
    while i<j:
        while(i<j and A[i]<A[l]):i+=1
        while(i<j and A[j]>A[l]):j-=1
        swap(A,i,j)
    if(i==j):
        swap(A,i-1,l)
        return i - 1
    else:
        swap(A,i,l)
        return i


def QuickSort(A,l,r):
    if(l<r):
        s = Partition(A,l,r)
        QuickSort(A,l,s-1)
        QuickSort(A,s+1,r)
    return A
A = [6,1,2,7,9,3,4,5,10]
T = QuickSort(A,0,len(A)-1)
print(T)