#-*-coding:utf-8-*-
"""
请实现两个函数，分别用来序列化和反序列化二叉树
"""
class Solution:
    def __init__(self):
        self.flag=-1
    def Serialize(self,root):
        if not root:
            return "#,"
        return str(root.val)+','+self.Serialize(root.left)+self.Serialize(root.right)
    def Deserialize(self,s):
        self.flag+=1
        l=s.split(',')
        if self.flag>=len(s):
            return None
        root=None
        if l[self.flag]!='#':
            root=TreeNode(int(l[self.flag]))
            root.left=self.Deserialize(s)
            root.right=self.Deserialize(s)
        return root