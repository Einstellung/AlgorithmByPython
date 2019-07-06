'''
一个链表中包含环，请找出该链表的环的入口结点。
'''

'''
首先使用MeetingNode判断这个链表有没有环，当有环的时候
进入EntryNodeOfLoop判断环的起始位置，需要知道环中节点数量，
然后两个指针相差环节点数量一起跑，当他们第一次相遇的时候，就是环
的起始位置
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def MeetingNode(self, pHead):
        if pHead == None:
            return None
        if pHead.next == None:
            return None
        
        pSlow = pHead.next
        pFast = pSlow.next
        
        while pFast:
            if pFast == pSlow:
                return pFast
            pFast = pFast.next
            pSlow = pSlow.next
            
            if pFast:
                pFast = pFast.next
        # 如果遍历到最后两个指针也没有相遇，那么这个链表
        # 是无环链表，故返回None
        return None
    
    
    def EntryNodeOfLoop(self, pHead):
        meetingNode = self.MeetingNode(pHead)
        
        # 如果meetingNode结果为None说明这个链表中没有环
        if meetingNode == None:
            return None
        
        # 判断环中节点数量
        # 这个结果可以用于接下来判断入口节点
        NodeLoop = 1
        flagNode = meetingNode
        while flagNode.next != meetingNode:   # 因为起始走了一步，接下来走n-1步就可以了，所以是用的flagNode.next
            NodeLoop += 1
            flagNode = flagNode.next 
            
        pFast = pHead
        
        for i in range(NodeLoop):
            pFast = pFast.next
            
        pSlow = pHead
        
        while pFast != pSlow:
            pFast = pFast.next
            pSlow = pSlow.next
        return pFast

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

s = Solution()
print(s.EntryNodeOfLoop(node1).val)