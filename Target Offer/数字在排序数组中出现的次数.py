'''
统计一个数字在排序数组中出现的次数。
例如，输入排序数组[1, 2, 3, 3, 3, 3, 4, 5]和数字3， 由于3在这个数组中出现了4次，
因此输出4
'''

# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # data是整数，如果想要判断最右侧和最左侧的k的值，如果k是整数的话
        # data的值刚好等于k的话，就没有办法知道是不是刚好是重复数字最右侧
        # 或者最左侧的值，所以用k+0.5来找最右侧的值，k-0.5来找最左侧的值
        # 然后做差，就可以知道一共出现了几次
        return self.Search(data, k+0.5) - self.Search(data, k-0.5)
    
    def Search(self, data, num):
        start = 0
        end = len(data) - 1
        
        while start <= end:
            # 用二分法来找最左侧和最右侧的值
            # 最右侧的话，最后start的位置会比k大一点的位置
            # 最左侧的话，最后start和k中最小的值是一样的位置
            mid = (start + end) // 2
            if data[mid] < num:
                start = mid + 1
            elif data[mid] > num:
                end = mid - 1
                
        return start

alist = [3,3,3,3,4,5]
s = Solution()
print(s.GetNumberOfK(alist, 3))