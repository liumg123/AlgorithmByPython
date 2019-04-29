# -*- coding:utf-8 -*-
"""
输入一棵二叉树，判断该树是否是平衡二叉树
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        left=self.TreeDepth(pRoot.left)
        right=self.TreeDepth(pRoot.right)
        return left+1 if left>right else right+1
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        left=self.TreeDepth(pRoot.left)
        right=self.TreeDepth(pRoot.right)
        if abs(left-right)>1:
            return False
        else:
            return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
        