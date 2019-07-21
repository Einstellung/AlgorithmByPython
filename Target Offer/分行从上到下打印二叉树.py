'''
从上到下按层打印二叉树，同一层的节点按照从左到右
的顺序打印，每一层打印到第一行，例如本题中上一个问题的二叉树
输出形式会是：
8
6 10
5 7 9 11
'''

'''
这道题和前面一道题十分类似，也可以用一个队列来保存要打印的节点。
为了把二叉树的每一行单独打印到一行里，我们需要两个变量：
一个变量表示当前层中还没有打印的节点数；另一个变量表示下一层节点数
'''
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
class Solution:
  def Print(self, root):
    if not root:
      return None
    
    queue = [root]
    toBePrinted = 1  # 表示当前层中还没有打印的节点数
    nextLevel = 0    # 表示下一层的节点数
    
    while len(queue) > 0:
      currentRoot = queue.pop(0)
      # 按空格隔开，不换行输出
      print(currentRoot.val, end=" ")
      
      if currentRoot.left:
        queue.append(currentRoot.left)
        nextLevel += 1
      if currentRoot.right:
        queue.append(currentRoot.right)
        nextLevel += 1
          
      toBePrinted -= 1
  
      # 如果当前层未打印的节点数为0，就跳转到下一层
      if toBePrinted == 0:
        # 如果下一层没有东西了，就不再执行程序了
        if nextLevel == 0:
          break
        print("\n")
        toBePrinted = nextLevel
        nextLevel = 0

pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
S.Print(pNode1)