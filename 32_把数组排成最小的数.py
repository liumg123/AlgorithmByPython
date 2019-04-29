# -*- coding:utf-8 -*-
"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""
"""
思路：比较两个字符串s1, s2大小的时候，先将它们拼接起来，比较s1+s2,和s2+s1那个大，如果s1+s2大，那说明s2应该放前面，所以按这个规则，s2就应该排在s1前面。

"""

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        numbers=list(map(str,numbers))
        n=len(numbers)
        for i in range(n):
            for j  in range(i,n):
                a=numbers[i]+numbers[j]
                b=numbers[j]+numbers[i]
                if a>b:
                    numbers[i],numbers[j]=numbers[j],numbers[i]
        ss=''
        print('numbers',numbers)
        for x in numbers:
            ss+=''.join(x)
        return ss
    
l1=[3,32,321]
l2=[3,5,1,4,2]
Solution().PrintMinNumber(l1)
        
        