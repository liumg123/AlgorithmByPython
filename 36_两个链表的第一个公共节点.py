# -*- coding:utf-8 -*-
"""
输入两个链表，找出他们的第一个公共节点
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def GetListLength(self,pHead):
        pNode=pHead
        length=0
        while pNode!=None:
            pNode=pNode.next
            length+=1
        return length
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        len1=self.GetListLength(pHead1)
        len2=self.GetListLength(pHead2)
        lenDiff=abs(len1-len2)
        if len2>len1:
            pHeadLong=pHead2
            pHeadShort=pHead1
        else:
            pHeadLong=pHead1
            pHeadShort=pHead2
        for i in range(lenDiff):
            pHeadLong=pHeadLong.next
        while pHeadLong!=None and pHeadShort!=None and pHeadLong!=pHeadShort:
            pHeadLong=pHeadLong.next
            pHeadShort=pHeadShort.next
        pCommonNode=pHeadLong
        return pCommonNode