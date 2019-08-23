'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if array == None or len(array) <= 0:
            return []
        resultExclusiveOr = 0
        # 从头到尾依次异或数组中的每个数字，最后得到的结果
        # 就是两个只出现一次的数字异或的结果
        for i in array:
            resultExclusiveOr ^= i
        
        # 找到第一个为1的位置，之后按照是否为1将数组分成两部分
        indexOf1 = self.FindFirstBitIs1(resultExclusiveOr)

        num1, num2 = 0, 0
        for j in range(len(array)):
            # 如果array[j]移动indexOf1之后为1，那么就将其归到num1中，否则是num2中
            if self.IsBit1(array[j], indexOf1):
                num1 ^= array[j]
            else:
                num2 ^= array[j]
        return [num1, num2]

    def FindFirstBitIs1(self, num):
        indexBit = 0
        # indexBit用来检验是否超出字符取值范围
        while num & 1 == 0 and indexBit <= 32:
            indexBit += 1
            num = num >> 1
        # 返回确定第几位字符为1
        return indexBit

    def IsBit1(self, num, indexBit):
        # 没有办法直接比较最后一位，右移之后才好比较
        num = num >> indexBit
        return num & 1


aList = [2, 4, 3, 6, 3, 2, 5, 5]
s = Solution()
print(s.FindNumsAppearOnce(aList))