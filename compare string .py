#!/usr/bin/env python
# coding: utf-8

# In[7]:


#写函数，不使用python内置函数，对一个长字符串进行排序。测试样例“loveneverfailsnomatteryoubelieveitornot”
#提示：字符串是可以比较大小的
#提示：本题有多种做法，但可以只提交一种 2023/4/5
s=input("请输入字符串:")
l=list(s)
def compare(L):
    
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[j]<=L[i]:
                L[i],L[j]=L[j],L[i]
                
    return (L)
S=(''.join(compare(l)))
print(S)

