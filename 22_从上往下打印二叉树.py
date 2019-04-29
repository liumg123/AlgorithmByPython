# -*- coding:utf-8 -*-
"""

从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        res=[root]
        res_value=[root.val]
        while res:
            cur_node=res.pop(0)
            if cur_node.left is not None:
                res.append(cur_node.left)
                res_value.append(cur_node.left.val)
            if cur_node.right is not None:
                res.append(cur_node.right)
                res_value.append(cur_node.right.val)
        return res_value