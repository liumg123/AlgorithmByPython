# -*- coding:utf-8 -*-
"""
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.list = []
        self.list1 = []
    def FindPath(self, root, expectNumber):
        if root==None:
            return self.list1
        self.list.append(root.val)
        expectNumber-=root.val
        if expectNumber==0 and root.left==None and root.right==None:
            new_list=[]
            for line in self.list:
                new_list.append(line)
            self.list1.append(new_list)
        self.FindPath(root.left,expectNumber)
        self.FindPath(root.right,expectNumber)
#         print('list',self.list.pop())
        self.list.pop()
        return self.list1