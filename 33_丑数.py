# -*- coding:utf-8 -*-
"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index<=0:
            return 0
        res=[1]*100000
        t2=0
        t3=0
        t5=0
        for i in range(1,index):
            res[i]=min(res[t2]*2,min(res[t3]*3,res[t5]*5))
            if res[i]==res[t2]*2:
                t2+=1
            if res[i]==res[t3]*3:
                t3+=1
            if res[i]==res[t5]*5:
                t5+=1
        return res[index-1]
        
Solution().GetUglyNumber_Solution(11) 