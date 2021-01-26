#全排列
def generateP(lst):
    result = []
    if len(lst)<=1:
        return [lst]

    for i in range(len(lst)):
        s = lst[:i] + lst[i+1:]
        p = generateP(s)
        for x in p:
            result.append(lst[i:i+1]+x)
    return result

#n皇后问题

if __name__ == "__main__":

    result = generateP([1,2,3])
    print(result)