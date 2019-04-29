# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        res=[1,1,2]
        if number==1:
            return 1
        elif number==0:
            return 0
        elif number>=3:
            while number >=3:
                res.append(res[-1]+res[-2])
                number-=1
#         for x in range(3,number):
#             res.append(res[-1]+res[-2])
            
        return res[-1]
