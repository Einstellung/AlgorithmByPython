'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''

# -*- coding:utf-8 -*-
class Solution:
    def fibonacci(self, n):
        res = [0, 1]
        
        while len(res) <= n:
            res.append(res[-1] + res[-2])

        return res[-1]

test = Solution()
print(test.fibonacci(100))
