"""在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。"""
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    #暴力求解，不考虑大小顺序关系
    def Find(self, target, array):
        # write code here
        row,col=len(array),len(array[0])
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                if array[i][j]==target:
                    return True
        return False
    #双指针法
    def Find1(self, target, array):
        row,col=len(array)-1,len(array[0])-1
        i=row
        j=0
        #双指针法，从左下角开始找，比左下角大则向右移动，j+=1，比左下角小，则向上移动，i-=1
        while j<=col and i>=0:
            if target>array[i][j]:
                j+=1
            elif target<array[i][j]:
                i-=1
            else:
                return True
        return False