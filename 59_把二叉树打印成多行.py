#-*-coding:utf-8-*-
"""
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""

class Solution:
    def Print(self,pRoot):
        if not pRoot:
            return []
        res=[]
        tmp=[pRoot]
        while tmp:
            length=len(tmp)
            row=[]
            for i in tmp:
                row.append(i.val)
            res.append(row)
            for i in range(length):
                node=tmp.pop(0)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
        return res