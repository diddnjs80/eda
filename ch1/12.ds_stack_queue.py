# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:09:26 2019

@author: shkim
"""

a = [1, 2, 3, 4, 5]
a.append(6)
print(a)

#%%
print(a.pop())
print(a)

#%%
print(a.pop(2)) # 인덱스 사용하여 pop 하도록...
#%%
print(a)


#%%

word = input("Input a word: ")
world_list = list(word)
print(len(world_list), world_list)


#%%
result = []
for _ in range(len(world_list)):  # _ 는 그냥 무시해줘라는 의미
    result.append(world_list.pop())

print('-' * 50)
print(result)
print(word[::-1]) # string을 꺼꾸로 돌리고 싶을 때 사용



