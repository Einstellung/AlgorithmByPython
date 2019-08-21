'''
假设一个单调递增的数组里的每个元素都是整数并且是唯一的。
请编程实现一个函数找出数组中任意一个数值等于其下标的元素。
例如，在数组{-3, -1, 1, 3, 5}中，数字3和它的下标相等。
'''


class Solution:
    def GetNumberSameAsIndex(self, data, num):
        if num < 0 or len(data) <= 0:
            return "please input right data or number"
        
        start = 0
        end = len(data) - 1
        while start <= end:
            mid = (start + end) // 2
            if data[mid] == num:
                return mid
            
            # 一个元素的值一旦大于他的下标，那么该元素右边的值
            # 肯定都大于他的下标。因此从改元素左边找就可以了
            elif data[mid] > mid:
                end = mid - 1

            # 同理，一个元素的值如果小于他的下标，
            # 那么左侧的值也都不满足条件
            elif data[mid] < mid:
                start = mid + 1
                
        return None

a = Solution()
a.GetNumberSameAsIndex([-3, -1, 1, 3, 5], 3)