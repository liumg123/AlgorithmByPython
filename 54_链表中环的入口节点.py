# -*- coding:utf-8 -*-
"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead==None or pHead.next==None:
            return None
        p1=pHead
        p2=pHead
        while p2!=None and p2.next!=None:
            p1=p1.next
            p2=p2.next.next
            if p1==p2:
                p2=pHead
                while p1!=p2:
                    p1=p1.next
                    p2=p2.next
                if p1==p2:
                    return p1
        return None