# -*- coding:utf-8 -*-
"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""
class Solution:
    # s字符串
    def isNumeric(self,s):
        #标记符号、小数点、指数是否出现
        sign=False
        decimal=False
        hasE=False
        for i in range(len(s)):
            if s[i]=='e'or s[i]=='E':
                if i==len(s)-1:return False#e后面一定要有数字
                if hasE==True:return False#不能有两个E
                hasE=True
            elif s[i]=='+' or s[i]=='-':
                #第二次出现+，-必须跟在e后
                if sign and s[i-1]!='e' and s[i-1]!='E':return False
                #第一次出现+，-且不是在字符串开头，也必须在e后
                if not sign and i>0 and s[i-1]!='e'and s[i-1]!='E':return False
                sign=True
            elif s[i]=='.':
                #e后面不能有小数点，且小数点不能出现两次
                if hasE or decimal:return False
                decimal=True
            elif s[i]<'0'or s[i]>'9':
                return False
        return True