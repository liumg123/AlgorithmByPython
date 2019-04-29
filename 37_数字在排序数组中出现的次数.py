# -*- coding:utf-8 -*-
"""
统计一个数字在排序数组中出现的次数。
"""
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        count=0
        for x in data:
            if x ==k:
                count+=1
        return count