#coding:utf-8
"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
"""
class Solution:
    def multiply(self,A):
        res=[]
        for i in range(len(A)):
            temp=1
            for j in range(len(A)):
                if i!=j:
                    temp*=A[j]
            res.append(temp)
        return res