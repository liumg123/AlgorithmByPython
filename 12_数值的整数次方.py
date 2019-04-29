# -*- coding:utf-8 -*-
"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
"""
class Solution:
    def Power(self, base, exponent):
        # write code here
        res=1
        e=abs(exponent)
        if base==0:
            return 0
        elif base>0:
            while e>0:
                res=res*base
                e-=1
            if exponent>=0:
                return res
            else:
                return float(1/res)
        else:
            while e>0:
                res=res*base
                e-=1
            if exponent%2==0:
                if exponent>0:
                    return -res
                else:
                    return float(1/res)
            else:
                if exponent>0:
                    
                    return res
                else:
                    return float(1/res)