def maxAscendingSum(nums):
    max = 0
    sum = 0
    for i in range(len(nums)):
        if i == 0:
            sum += nums[i]
            continue
        if nums[i] > nums[i - 1]:
            sum += nums[i]
        else:
            if sum > max:
                max = sum
            sum = 0
            sum += nums[i]
    if sum > max:
        max = sum
    print(max)
    return max
'''
[[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
'''
from sortedcontainers import SortedList
def  getNumberOfBacklogOrders(orders):
    backlogOrder_sell = []  #采购的积压订单
    backlogOrder_buy = []  #销售的积压订单
    backlogOrder_sell = SortedList(backlogOrder_sell)
    backlogOrder_buy = SortedList(backlogOrder_buy)
    for i in range(len(orders)):
        price,amount,orderType = orders[i] #订单i的信息
        if orderType == 0:#表明这是一个采购的订单
            while len(backlogOrder_buy) != 0 and backlogOrder_buy[0][0] <= price or amount == 0:
                if backlogOrder_buy[0][1] > amount:#如果销售订单的最低价小于采购价格
                    backlogOrder_buy[0][1] -= amount #充足
                    amount = 0
                    break
                else:
                    amount -= backlogOrder_buy[0][1]
                    backlogOrder_buy.pop(0)  #相等删除

            if amount != 0:
                backlogOrder_sell.add([price,amount,orderType])#加入积压订单
        else:#这是一个销售订单
            while len(backlogOrder_sell) != 0 and backlogOrder_sell[-1][0] >= price or amount == 0:#如果采购订单最大价格大于销售的价格，删除采购订单
                if backlogOrder_sell[-1][1] > amount:
                    backlogOrder_sell[-1][1] -= amount
                    amount = 0
                    break
                else:
                    amount -= backlogOrder_sell[-1][1]
                    backlogOrder_sell.pop(-1)

            if amount != 0:
                backlogOrder_buy.add([price,amount,orderType]) #加入积压订单
    amounts = sum(x[1] for x in backlogOrder_sell)
    amounts += sum(x[1] for x in backlogOrder_buy)
    print(amounts%(pow(10,9) + 7))
    return amounts%(pow(10,9) + 7)

class Solution:#应该是模拟平衡二叉树 
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l = [int(maxSum / n) for i in range(n)]
        s = maxSum % n
        l[index] += 1
        s -= 1

        return l[index]
