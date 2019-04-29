#-*-coding:utf-8-*-
"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        #栈A用来入队列
        #栈B用来出队列，当栈B为空时，栈A全部出栈到B，B在出栈（即出队列）
        self.stackA=[]
        self.stackB=[]
    def push(self, node):
        # write code here
        self.stackA.append(node)
    def pop(self):
        # return xx
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()
        
        