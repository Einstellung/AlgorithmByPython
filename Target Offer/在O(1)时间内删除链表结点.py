'''
给定单向链表的头指针和一个结点指针,定义一个函数在O(1)时间删除该结点
'''
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None
    def __del__(self):
        self.val = None
        self.next = None

class Solution:
    def DeleteNode(self, pListHead, pToBeDeleted):
        if not pListHead or not pToBeDeleted:
            return None

        # 要删除的节点不是尾节点
        if pToBeDeleted.next != None:
            pNext = pToBeDeleted.next
            pToBeDeleted.val = pNext.val     # 要删除节点内容被后一个节点内容覆盖
            pToBeDeleted.next = pNext.next   # 要删除节点指针指向后一个节点的后一个节点
            pNext.__del__()                  # 删除后一个节点

        # 链表只有一个节点，删除头结点(也是尾节点)
        elif pListHead == pToBeDeleted:
            pToBeDeleted.__del__()
            pListHead.__del__()

        # 链表中要删除的节点为尾节点时，删除尾节点
        # 之所以要分开来的原因在于尾节点之后没有节点，所以不能按照第一种情况进行操作  
        else:
            pNode = pListHead
            while pNode.next != pToBeDeleted:
                pNode = pNode.next
            # 之所以要遍历的原因在于不知道尾节点的前一个节点是什么
            # 单向链表没有办法向前找，所以要遍历完最后next为None    
            pNode.next = None              
            pToBeDeleted.__del__()


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(15)
node1.next = node2
node2.next = node3
node3.next = node4

S = Solution()
S.DeleteNode(node1, node3)
print(node3.val)
S.DeleteNode(node1, node3)
print(node3.val)
print(node2.val)
S.DeleteNode(node1, node1)
print(node1.val)
S.DeleteNode(node1, node1)
print(node1.val)
