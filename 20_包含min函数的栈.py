# -*- coding:utf-8 -*-
"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

"""
class Solution:
    def __init__(self):
        self.stack=[]
    def push(self, node):
        # write code here
        self.stack.append(node)
    def pop(self):
        # write code here
        self.stack.pop()
    def top(self):
        # write code here
        self.stack.pop(0)
    def min(self):
        # write code here
        return min(self.stack)