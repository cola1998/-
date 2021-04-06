from sortedcontainers import SortedList
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # n = len(nums)
        # if n < 3: return False
        #
        # left_min = nums[0]  #左侧最小元素
        # right_all = SortedList(nums[2:]) #右侧所有元素
        # for j in range(1,n-1):#枚举j的可能取值
        #     if left_min < nums[j]:#只有nums[i]<nums[j]时，才需要寻找k
        #         index = right_all.bisect_right(left_min) #记录nums[i]在右侧的位置 在该位置右边寻找k
        #         if index < len(right_all) and right_all[index] < nums[j]: #如果在right_all中有比nums[i]大的数据,并且小于nums[j]
        #             return True
        #     left_min = min(left_min,nums[j])#否则更新left_min
        #     right_all.remove(nums[j+1])
        # return False

        n = len(nums)  #O(n^2)会超时
        if n < 3: return False
        left_min = nums[0]
        for j in range(1, n-1):  # 枚举j的可能取值
            for k in range(j+1,n):
                if nums[j] > nums[k] and left_min < nums[k]:
                    return True
            left_min = min(left_min,nums[j])
        return False