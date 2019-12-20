# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:26:38 2019

@author: shkim
"""

# empty dictionary
d1 = {}
d2 = dict()

print(type(d1), d1, type(d2), d2)

#%%
info = {1:'kim', 2:'park'}
print(info)

info[1]='lee'
print(info)

#%%
info = {'name':'kim', 2:'park'}
print(info)

info['name']='lee'
print(info)

#%%
print(info.keys())
print(info.values())
print(info.items())

#%%
for k,v in info.items():
    print(k,v)