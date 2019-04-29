# -*- coding:utf-8 -*-
"""
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
"""
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        temp=[x for x in s if s.count(x)==1]
        if len(temp)>0:
            return s.index(temp[0])
        return -1