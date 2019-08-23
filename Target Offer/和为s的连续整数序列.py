'''
输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。
例如，输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以打印三个连续
序列，1-5,4-6,7-8
'''

class Solution:
    def FindContinuousSequence(self, num):
        # 要求至少是连续两个正数，所以输入的num不可能比3小
        if num < 3:
            return None
        
        small, big = 1, 2
        # 要求是连续的数，所以最大的数也只能是比num一半多一点
        middle = num // 2 + 1
        SumNum = 0  # 用来计算small和big以及之间的数的和
        
        while big <= middle and small < big:
            SumNum = self.CalculateSum(small, big)

            # 如果找到就打印
            if SumNum == num:
                self.PrintContinuousSequence(small, big)
                # 找到之后增加big来找下一个
                big = big + 1
                SumNum = self.CalculateSum(small, big)
            # 如果小就扩大序列    
            if SumNum < num:
                big = big + 1
            # 如果大就缩小序列
            if SumNum > num:
                small = small + 1

    # 用来计算small和big之间数的和
    def CalculateSum(self, small, big):
        Sum = 0
        for i in range(small, big+1):
            Sum = Sum + i

        return Sum

    # 用来进行打印           
    def PrintContinuousSequence(self, small, big):
        for i in range(small, big + 1):
            print(i)


test = Solution()
test.FindContinuousSequence(15)