"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        res=[1,1,2]
        if number==1:
            return 1
        elif number==2:
            return 2
        elif number>=3:
            while number >=3:
                res.append(res[-1]+res[-2])
                number-=1
#         for x in range(3,number):
#             res.append(res[-1]+res[-2])
            
        return res[-1]
        
Solution().jumpFloor(4)       