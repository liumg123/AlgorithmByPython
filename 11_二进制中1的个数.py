# -*- coding:utf-8 -*-

"""输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。"""
class Solution:
    def intToBin32(self, i):
        return (bin(((1 << 32) - 1) & i)[2:]).zfill(32)
    def NumberOf1(self, n):
        # write code here
        if n>=0:
            return str(bin(n))[2:].count('1')
        else:
            return (self.intToBin32(n).count('1'))
Solution().NumberOf1(-3)