'''
请实现两个函数，分别用来序列化和反序列化二叉树。这里没有规定序列化的方式。
使用前序遍历的方式来顺序化二叉树要效果好
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
       
    
class Solution:
    def Serialize(self, root):
        if not root:
            return "#"
        
        return str(root.val) + "," + self.Serialize(root.left) + "," + self.Serialize(root.right)
    
    def Deserialize(self, s):
        list = s.split(",")
        return self.deserializeTree(list)
    
    def deserializeTree(self, list):
        # list遍历结束时
        if len(list) <= 0:
            return None
        val = list.pop(0)
        root = None
        
        if val != "#":
            root = TreeNode(int(val))
            root.left = self.deserializeTree(list)
            root.right = self.deserializeTree(list)
            
        return root        

pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode3.left = pNode5
pNode3.right = pNode6

S = Solution()
serialize = S.Serialize(pNode1)
print(serialize)
des = S.Deserialize(serialize)
des.left.val