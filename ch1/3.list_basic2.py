# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 10:33:23 2019

@author: shkim
"""

"""
k_s = [10, 20, 30, 40]
m_s = [11, 22, 33, 44]
e_s = [50, 60, 70, 80]

a = [9, 2, 7, 4, 6]
b = [11, 22, 33, 44, 55, 66]
"""


#%%
# unpacking
t=[1,2,3]
a,b,c = t
print(a,b,c,t)
print(type(a),type(t))

#%%
t2 = t, a,b
t3 = [t, a,b]
print(t2)
print(type(t2))
print(type(t3))
#%%

k_s = [10, 20, 30, 40]
m_s = [11, 22, 33, 44]
e_s = [50, 60, 70, 80]

m_s = [k_s,m_s, e_s]

print(m_s)
print(m_s[1][1])

m_s[0][2] = 35
print(m_s) 

#%%
a=300
b=300

print(a==b)
print(a is b)
#%%

a = [2,1,5,6]
b=[11,55,22]
print(a,b)
print(a.__add__, b.__add__)
b=a
print(a.__add__, b.__add__)
print(b)
a[1]=100
print(b)
#%%
b.sort()
print(b)
print(a)

#%%
a = [2,1,5,6]
b=[11,55,22]
print(a,b)
print(a.__add__, b.__add__)

b = a.copy()
print(a,b)
print(a.__add__, b.__add__)
a[1]=100
print(b)