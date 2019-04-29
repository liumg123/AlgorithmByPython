# -*- coding:utf-8 -*-
"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""

class Solution:
    
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if  sequence==None or len(sequence)==0 :
            return False
        if len(sequence)==1 :
            return True
        #后序中最后一个节点是根节点，二叉查找树中左子树节点小于根节点，右子树节点大于根节点
        root=sequence[-1]
#         left=[x for x in sequence if x <root]
#         right=[x for x in sequence if x >root]这样构造会使得right中的元素可能大于left的元素
        left_index=0
        while sequence[left_index]<root:
            left_index+=1
        
        for j in range(left_index,len(sequence)-1):
            if sequence[j]<root:
                return False
        left=sequence[0:left_index]
        right=sequence[left_index:len(sequence)-1]
        left_flag=True
        if len(left)>0:
            left_flag=self.VerifySquenceOfBST(left)
            print('left_flag',left_flag,left)
        right_flag=True
        if len(right)>0:
            right_flag=self.VerifySquenceOfBST(right)
            print('right_flag',right_flag,right)
        return left_flag and right_flag
l1=[1,4,7,6,3,13,14,5,8]
l2=[]
Solution().VerifySquenceOfBST(l1)   