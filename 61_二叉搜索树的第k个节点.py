# -*- coding:utf-8 -*-
"""
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def NodeValue(self,pRoot):
        if not pRoot :
            return None
        self.NodeValue(pRoot.left)
        res.append(pRoot)
        self.NodeValue(pRoot.right)
        return res
    def KthNode(self, pRoot, k):
        # write code here
        global res
        res=[]
        self.NodeValue(pRoot)
        if len(res)<k or k<=0:
            return 
        return res[k-1]