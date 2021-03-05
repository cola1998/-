#codeup1918  简单计算器
# 30/90-26+97-5-6-13/88*6+51/29+79*87+57*92

def getOp(x,y):
    if x == '+' or x == '-' and y == '*' or y == '/':
        return -1
    elif x == '+' or x == '-' and y == '+' or y == '-':
        return 0
    elif x == '*' or x == '/' and y == '*' or y == '/':
        return 0
    else:
        return 1
if __name__ == '__main__':
    ll = []
    while(True):
        l = input()
        if(l == '0'):
            break
        else:
            ll.append(l)
    for l in ll:
        l = l.split(' ')
        for i in l:
            if i == '+' or i == '-' or i == '*' or i == '/':
                pass
