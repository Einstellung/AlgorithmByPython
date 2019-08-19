'''
在一个字符串(1<=字符串长度<=10000，全部由大写字母组成)中找到第一个只出现一次的字符。
'''

# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, string):
        if len(string) <= 0 or string == None:
            return 0
        
        alphabet = {}
        
        
        # 注意字典是无序的，所以没有办法找到第一次出现的字母
        # 但是string字符串很好的保留了顺序
        for i in string:
            if i not in alphabet.keys():
                alphabet[i] = 1
                # 防止后面再+1，所以第一次找到直接就跳出本次判断
                continue 
                
            alphabet[i] += 1
            
        for i in string:
            if alphabet[i] == 1:
                return i
   
        return 0

test = Solution()
print(test.FirstNotRepeatingChar("abaccdeff"))