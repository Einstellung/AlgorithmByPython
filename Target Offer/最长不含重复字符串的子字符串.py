'''
请从字符串中找出一个最长的不包含重复字符的子字符串，
计算该最长子字符串的长度。假设字符串中只包含"a-z"的字符。
'''



class Solution:
    def longestSubstringWithoutDuplication(self, string):
        if len(string) <= 0:
            return None
        
        # start指针用来存放第一个不重复字符串的索引
        res, start, n = 0, 0, len(string)
        maps = {}  # 设置字典加速重复字符查找速度
        
        for i in range(n):
            # 如果当前字符重复了，就加1指向新的字符，如果不重复就不动
            start = max(start, maps.get(string[i], -1) + 1) 
            
            # 始终计算和保存最长子字符串的长度
            res = max(res, i - start + 1)
            
            # 将当前字符与其在 input 中的 index 记录下来，便于start索引是否是重复字符
            maps[string[i]] = i
            
        return res
s = Solution()
string = "arabcacfr"
s.longestSubstringWithoutDuplication(string)