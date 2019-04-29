# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead == None:
            return 
        head = pHead
        #复制每个节点，如复制节点A得到A1,将A1插入到A后面
        while head:
            nd = RandomListNode(0)
            nd.label = head.label
            nd.next = head.next
            head.next = nd
            head = nd.next
            
        #遍历链表，A1.random=A.random.next    
        head = pHead
        while head:
            nd = head.next
            if head.random != None:
                nd.random = head.random.next
            head = nd.next
        #将链表拆分为原链表和复制后的链表
        head = pHead
        nHead =  head.next
        nNode = head.next
        head.next = nNode.next
        head = head.next
        while head :
            nNode.next = head.next
            nNode = nNode.next
            head.next = nNode.next
            head = head.next
        return nHead
