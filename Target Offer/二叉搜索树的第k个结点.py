'''
给定一颗二叉搜索树，请找出其中的第k大的结点。例如，
    5
   / \
  3  7
 /\ /\
2 4 6 8 中，
按结点数值大小顺序第三个结点的值为4。
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        # count用来计数，确保找到第k个节点
        self.count = 0

    def KthNode(self, pRoot, k):
        if not pRoot:
            return None

        # node用来将节点的val传递出来，避免遍历整个二叉搜素树，增大计算开销
        # 这个函数有三种情况会有返回值，第一种是遍历到根的位置返回None，第二种是
        # 返回找到的val值，如果返回None的时候，node始终为None，所以不会触发return node
        # 当返回val的时候，此时node有值，通过返回而不是继续递归，很快就可以跳出来了
        
        # 如果一个函数执行的时候，没有任何返回值，那么最终执行结束之后就会向上返回一个None
        # 因此node返回触发机制是只有val有值返回的时候才会触发
        node = self.KthNode(pRoot.left, k)
        if node:
            return node
        self.count += 1
        if self.count == k:
            return pRoot.val
        node = self.KthNode(pRoot.right, k)
        if node:
            return node


pNode1 = TreeNode(5)
pNode2 = TreeNode(3)
pNode3 = TreeNode(7)
pNode4 = TreeNode(2)
pNode5 = TreeNode(4)
pNode6 = TreeNode(6)
pNode7 = TreeNode(8)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

a = Solution()
print(a.KthNode(pNode1, 3))