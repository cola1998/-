# 201709-1
# n = int(input())
# count = 0
# while n!=0:
#     if n>=50:
#         n -= 50
#         count += 7
#     elif n>=30:
#         n -= 30
#         count += 4
#     else:
#         count += int(n/10)
#         n -= n
# print(count)

# 201709-2
# n, k = map(int, input().split())
# keyL = [i for i in range(1, n + 1)]
# timeTable = []
# # tag=0表示归还  1表示借
# for i in range(k):
#     id, st, lt = map(int, input().split())
#     timeTable.append((st,True,id))
#     timeTable.append((st+lt,False,id))
# timeTable.sort()
# for time,take,id in timeTable:
#     if take: #需要归还
#         keyL[keyL.index(id)] = 0
#     else:
#         keyL[keyL.index(0)] = id
#     print(keyL)
#
# print(" ".join(map(str,keyL)))

# n, k = map(int, input().split())
# keyL = [i for i in range(1, n + 1)]
# timeTable = {}
# # tag=0表示归还  1表示借
# for i in range(k):
#     id, st, lt = map(int, input().split())
#     if st in timeTable:
#         timeTable[st].append([id,False]) #借出
#     else:
#         timeTable[st] = [[id,False]]
#
#     if st + lt in timeTable:
#         timeTable[st+lt].append([id, True]) #归还
#     else:
#         timeTable[st+lt] = [[id, True]]
# timet = sorted(timeTable)
#
# for time in timet:
#     for id,take in timeTable[time]:
#         if take: #需要归还
#             keyL[keyL.index(0)] = id
#         else:
#             keyL[keyL.index(id)] = 0
#
# print(" ".join(map(str,keyL)))

#201709-3
import json
n,m = map(int,input().split())
jsonS = ""
for i in range(n):
    jsonS = jsonS + input()
print(jsonS)
json_dict = json.loads(jsonS)
print(json_dict)
for i in range(m):
    q = input()
    print(type(json_dict[q]))
    if isinstance(json_dict[q],str):
        print("STRING {0}".format(json_dict[q]))
    else:
        print("OBJECT")