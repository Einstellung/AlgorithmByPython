'''
输入一个整型数组,数组里有整数也有负数。
数组中一二或连续的多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)
'''

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if len(array) <= 0 or array == None:
            return 0
        
        result = array[0]  # 用来保存子数组中和的最大值
        accumulation = 0   # 用来保存累加和，初始值为0
        for i in range(1, len(array)):
            num = array[i]
            
            # 如果累加的和小于0，就把累加和清空，之后赋值给下一个num
            if accumulation < 0:
                accumulation = 0
            accumulation += num    
             
            # 如果最大的数值小于累加和，就把累加和赋值给结果result
            if result < accumulation:
                result = accumulation
                
        return result

    # 动态规划解决问题
    def FindGreatestSumOfSubArray2(self, array):
        if array == None or len(array) <= 0:
            return 0
        aList = [0]*len(array)
        for i in range(len(array)):
            if i == 0 or aList[i-1] <= 0:
                aList[i] = array[i]
            else:
                aList[i] = aList[i-1] + array[i]
        return max(aList)



alist = [1, -2, 3, 10, -4, 7, 2, -5]
s = Solution()
print(s.FindGreatestSumOfSubArray2(alist))