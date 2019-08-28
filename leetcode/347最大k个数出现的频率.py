'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''


'''
题目自己限定了k一定是合法的，所以不可能出现两个数字出现频率相同的情况

思路就是我们先把对应的数字和其出现频次放到一个map里面，然后对这个maps里面的value()集合做一个for loop，这样我们就可以得到一个list，
list里面的每一个元素代表的就是count为该对应index的key（即数字）的集合


k = 2
nums = [1,1,1,2,2,3,4,4]时，

我们的maps就是{1: 3, 2: 2, 3: 1},
然后我们新建一个buckets，
- count为3的数字有1，我们就令bucktes[3] = [1], 
- count为2的数字有2和4，我们就令buckets[2] = [2,4]
- count为1的数字有3，我们就令buckets[1] = [3]


最后我们从bucktes的最后一个元素开始遍历，如果该元素不为初始化的'*'的话,我们就把当前元素（type list）的元素全部extend到res中去，最后返回res
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        res, maps, buckets = [], collections.Counter(nums), ['*'] * (len(nums)+1)

        for key, count in maps.items():
            # 这里的count既表示字典的值，也表示数组的位置，也就是在对数数组
            # 位置上面插入元素，很好的实现了查找大小关系和对应元素
            if buckets[count] == '*':
                buckets[count] = []
            buckets[count].append(key)

        i = len(nums)
        while len(res) < k and i >= 0:
            if buckets[i] != '*':
                res.extend(buckets[i])
            i -= 1
        return res

a = Solution()
nums = [1,1,1,2,2,3]
# nums = [1,2]
a.topKFrequent(nums, 2)