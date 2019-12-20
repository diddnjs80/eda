# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:37:58 2019

@author: shkim
"""

"""
# Tuple
"""
#%%

t = (1,2,3,4,5)
print(t, type(t))
print(t[0],t[1:3], t[-1])
#t[1] = 20 # 값을 바꾸지 못함..!!!!!

print(t+t, t*2)




#%%
"""
# Set
"""
#%%
s = {1,2,3,1,4,3} # set은 중복된 요소를 제거함
print(s, type(s))
s.update([4,5,6,7,7])
print(s)
s.clear()
print(s)

#%%
s1 = {} # 딕셔너리이다
print(type(s1))
s2 = set()
print(type(s2))
s3 = set([1,1,2,3,4,4])
print(type(s1), type(s2),type(s3),s1,s2,s3)

#%%
# 합집합
s1 = set([1,2,3,4,5])
s2 = {3,4,5,6,7}
s3 = s1.union(s2)
print(s1.union(s2))
print(s3)



#%%
# 교집합
s1 = set([1,2,3,4,5])
s2 = {3,4,5,6,7}
s3 = s1.intersection(s2)
s4 = s1 & s2
print(s1.intersection(s2))
print(s3, s4)

#%%
# 차집합
s1 = set([1,2,3,4,5])
s2 = {3,4,5,6,7}
s3 = s1.difference(s2)
s4 = s1 -s2
print(s1.difference(s2))
print(s3, s4)









