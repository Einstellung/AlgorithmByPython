'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def __init__(self):
        self.flag = True
        
    def IsBalanced_Solution(self, pRoot):
        self.getDepth(pRoot)
        return self.flag
    
    def getDepth(self, pRoot):
        if pRoot == None:
            return 0
        
        # 这是后续遍历的特点
        left = self.getDepth(pRoot.left) + 1
        right = self.getDepth(pRoot.right) + 1
        
        # 判断该子树的左右节点长度是否超过1，即判断
        # 该子树是否为平衡二叉树，每个子树都是平衡二叉树
        # 那么总体也是平衡二叉树
        if abs(left - right) > 1:
            self.flag = False
        
        # 如果一个节点有多个分支，要取最长分支
        # 只有最长的分支才是二叉树的深度
        return max(left, right) 

pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(7)
pNode7 = TreeNode(6)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode5.left = pNode6
pNode3.right = pNode7

a = Solution()
a.IsBalanced_Solution(pNode1)