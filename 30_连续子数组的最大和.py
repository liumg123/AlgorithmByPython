# -*- coding:utf-8 -*-
"""
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
"""
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        n=len(array)
        if array==None or len(array)==0:
            return 0
        flag=False
        curSum=0
        nGreatstSum=float("-inf")
        for i in range(n):
            #若和为负数，抛弃之前计算的结果把当前值赋给curSum，从新计算
            if curSum<=0:
                curSum=array[i]
            else:
                curSum+=array[i]
            print(i,curSum)
            #把计算的最大值保存下来
            if curSum>nGreatstSum:
                nGreatstSum=curSum
        return nGreatstSum
Solution().FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5])