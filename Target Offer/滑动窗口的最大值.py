'''
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
他们的最大值分别为{4,4,6,6,6,5}；
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
'''

# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, array, num):
        if not array or num <= 0:
            return []
        
        queue = [] # queue用来存储array每个元素的位置
        result = [] # 用来保存最后弹出的元素
        
        for i in range(len(array)):
            # 如果滑动窗口已经滑出queue的头部元素的位置，
            # 则弹出头部元素
            if len(queue) > 0 and i+1-num > queue[0]:
                queue.pop(0)
            
            # 如果新加入的数字比已有的数字大，已有的数字剔除
            while len(queue) > 0 and array[queue[-1]] < array[i]:
                queue.pop()
            # 新加入的数字如果比已有的数字小，不管，其实就是
            # 新加入数字小的话，就加进去
            queue.append(i)
            
            # 滑动窗口的最大值总是位于头部的
            if i >= num-1:
                result.append(array[queue[0]])
                
            i += 1
            
        return result

test = [2, 3, 4, 2, 6, 2, 5, 1]
s = Solution()
print(s.maxInWindows(test, 3))

