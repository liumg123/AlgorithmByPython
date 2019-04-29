#coding:utf-8
"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

时间复杂度过大，超时
"""
#归并排序
count=0
class Solution:
    
    def InversePairs(self, data):
        global count
        def merge_sort(data):
            if len(data)==1:
                return data
            mid=len(data)//2
            left=merge_sort(data[:mid])
            right=merge_sort(data[mid:])
            return merge(left,right)
        def merge(left,right):
            global count
            l,r=0,0
            result=[]
#             print('left,right',left,right)
            while len(left)>l and len(right)>r:
                if left[l]<=right[r]:
#                     print('0,l,r,left[l],right[r],result,count',l,r,left[l],right[r],result,count)
                    result.append(left[l])
                    l+=1
                else:
#                     print('1,l,r,left[l],right[r],result,count',l,r,left[l],right[r],result,count)
                    count+=len(left)-l
                    result.append(right[r])
                    r+=1
            result+=left[l:]
#             count+=len(left[l:])-1
            result+=right[r:]
            return result
        merge_sort(data)
        print(merge_sort(data))
        return count//2%1000000007
l1=[1,2,3,4,5,6,7,0]
l2=[364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]

Solution().InversePairs(l2)
                    