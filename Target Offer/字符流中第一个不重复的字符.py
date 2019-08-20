'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
如果当前字符流没有存在出现一次的字符，返回#字符。
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.alist = []
        self.adict = {}
        
    def FirstAppearingOnce(self):
        # 当列表中的首字符重复出现，就将其剔除列表
        while len(self.alist) > 0 and self.adict[self.alist[0]] > 1:
            self.alist.pop(0)
        if len(self.alist) == 0:
            return "all chars are repeated"
        else:
            return self.alist[0]
            
    
    def Insert(self, char):
        # 注意输入的是字符流，而不一定是字母
        # 所以不能用isalpha来判断
#         if not char.isalpha():
#             return "please input char"
        if not char:
            return "please input char"
        # 同上一个题一样，需要一个字符一个字符来导入字典进行判断
        for i in char:
            self.alist.append(i)
            if i not in self.adict.keys():
                self.adict[i] = 1
            else:
                self.adict[i] += 1