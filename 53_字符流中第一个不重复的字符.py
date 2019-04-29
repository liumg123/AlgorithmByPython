# -*- coding:utf-8 -*-
"""
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
"""
class Solution:
    # 返回对应char
    def __init__(self):
        self.s=""
    def FirstAppearingOnce(self):
        # write code here
        print('s',self.s)
        #res=[x for x in list(set(self.s)) if self.s.count(x)==1]
        res=list(filter(lambda c:self.s.count(c)==1,self.s))
        return res[0] if res else "#"
            
    def Insert(self, char):
        # write code here
        self.s+=char