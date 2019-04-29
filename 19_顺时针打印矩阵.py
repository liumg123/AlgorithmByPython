# -*- coding:utf-8 -*-
"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        
        if not matrix:
            return []
        res=[]
        r1=0
        r2=len(matrix)-1#行数
        c1=0
        c2=len(matrix[0])-1#列数
        while r1<=r2 and c1<=c2:
            for c in range(c1,c2+1):
                res.append(matrix[r1][c])#将上面的行加入
            print('res',res)
            for r in range(r1+1,r2+1):
                res.append(matrix[r][c2])#将右边的列，向下加入
            print('res',res)
            if r1<r2 and c1<c2:
                for c in range(c2-1,c1,-1):
                    res.append(matrix[r2][c])#将下面的行，向左顺序加入
                print('res',res)
                for r in range(r2,r1,-1):
                    res.append(matrix[r][c1])#将左边的列，从下往上加入
                print('res',res)
            r1+=1
            r2-=1
            c1+=1
            c2-=1
        return res

        
        
        
        
Solution().printMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])