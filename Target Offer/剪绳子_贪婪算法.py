'''
通过归纳总结的办法可以发现，要想使得各段绳子长度乘积最大，当n>=5时，我们尽可能多剪绳长度为3的绳子
当剩余绳子长度为4的时候就不再剪了。对于某些质数而言，余数可能不会是4，而是2，那么就把这种余数为2的单独作为一种情况返回即可
'''

class Solution:
    def maxProductAfterCutting_solution2(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 3
        
        timesOf3 = length // 3
        
        if length - timesOf3*3 == 1:
            timesOf3 -= 1
            return pow(3, timesOf3)*pow(4, 1)
        if length - timesOf3*3 == 2:
            return pow(3, timesOf3)*pow(2, 1)

test = Solution()
test.maxProductAfterCutting_solution2(8)