# -*- coding:utf-8 -*-
"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
"""
class Solution:
    def Permutation(self, ss):
        # write code here 
        res=[]
        if len(ss)<2:
            return ss.split()
        for i in range(len(ss)):
            for n in map(lambda x:x+ss[i],self.Permutation(ss[:i]+ss[i+1:])):
                if n not in res:
                    res.append(n)
#             print(list(map(lambda x:x+ss[i],self.Permutation(ss[:i]+ss[i+1:]))))
        return sorted(res)
        
Solution().Permutation('abc')