'''
假设把某股票的价格按照时间先后顺序存储在数组中，
请问买卖该股票一次可获得的最大利润是多少？

例如，一只股票在某些时间节点的价格为{9,11,8,5,7,12,16,14}。
如果我们能在价格为5的时候买入并在价格为16时卖出，则能获得最大的利润为11
'''

'''
这个题的思路是如果扫描到数组的第i个数字时，只要我们能够记住之前的i-1个数字
的最小值，就能算出当前价位卖出时可能得到的最大利润。
'''

class Solution:
    def MaxDiff(self, array):
        if array == None or len(array) <= 0:
            return None
        
        MinNumber = array[0]
        MaxDiff = 0
        
        for i in range(1, len(array)):
            
            if MinNumber > array[i]:
                MinNumber = array[i]
            if MaxDiff < array[i] - MinNumber:
                MaxDiff = array[i] - MinNumber

                
        return MaxDiff


a = Solution()
array = [9, 11, 8, 5, 7, 12, 16, 14]
a.MaxDiff(array)