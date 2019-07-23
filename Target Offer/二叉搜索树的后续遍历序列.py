'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
二叉搜索树对于每一个非叶子节点, 均有结点左子节点<当前节点<结点右子节点
'''

# -*- coding:utf-8 -*-
class Solution:
    def VerifySequenceOfBST(self, sequence):
        if not sequence or sequence == []:
            return False
        
        length = len(sequence)
        root = sequence[-1] 
        index = 0
        
        while index < length-1:
            if sequence[index] > root:
                break
            index += 1
        
        # index这时候实际上可以看成是右子树的第一个节点了
        right_index = index
        while right_index < length-1:
            if sequence[right_index] < root:
                return False
            right_index += 1
        
        left = True
        if index > 0:
            left = self.VerifySequenceOfBST(sequence[:index])
            
        right = True
        # 右子节点至少有一个值
        if index < length-1:
            right = self.VerifySequenceOfBST(sequence[index:length-1])
            
        return left and right  

array = [5, 7, 6, 9, 11, 10, 8]
array2 = [4, 6, 7, 5]
array3 = [1, 2, 3, 4, 5]
S = Solution()
print(S.VerifySequenceOfBST(array))
print(S.VerifySequenceOfBST(array2))
print(S.VerifySequenceOfBST(array3))  