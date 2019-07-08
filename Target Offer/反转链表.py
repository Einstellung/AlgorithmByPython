'''
反转链表
输入一个链表，反转链表后，输出链表的所有元素
'''

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        pReversedHead = None  # 反转之后链表的头结点
        pNode = pHead         # 节点i本身
        pPrev = None          # 节点i的前一个节点

        # 需要对头结点是否为空进行一个判断
        while pNode != None:  
            pNext = pNode.next  # 节点i的后一个节点

            # 当遍历到尾节点之后，将其赋值为反转之后的头节点
            # 这也是对链表是否有一个节点的判断
            if pNext == None:
                pReversedHead = pNode

            pNode.next = pPrev  # 将节点i的next节点指向其前一个节点
            pPrev = pNode       # 将节点i赋值给PPre保存，便于下一次指向前一个节点
            pNode = pNext       # 将节点i下一次变化之前把节点j保存起来，防止节点j找不到节点i
        return pReversedHead    # 返回反转之后的链表
    # 递归实现反转链表
    def ReverseListRec(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        else:
            pReversedHead = self.ReverseList(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
            return pReversedHead

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

S = Solution()
p = S.ReverseList(node1)
print(p.next.val)