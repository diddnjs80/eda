# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 21:09:06 2019

@author: shkim
"""
#%%
"""
# 리스트값에 인덱스를 붙여 출력: enumerate( ) 함수 
"""
#%%
color = ['red', 'blue', 'white', 'black']
d_c = {i:j for i,j in enumerate(color) }
print(d_c)

#%%
"""
# 리스트값을 병렬로 묶어 출력: zip( ) 함수
"""
#%%
# zip 병렬로 자료를 연결하는 함수
color = ['red', 'blue', 'white', 'black']
cnt = [6, 2, 3, 7]
# {'red': 6, 'blue': 2, 'white': 3, 'black': 7}
col_cnt = {i:j for i, j in zip(color, cnt)}
print(col_cnt)

#%%
# [['red', 6], ['blue', 2], ['white', 3], ['black', 7]]
col_cnt = .......
print(col_cnt)

#%%
"""
(1, 3, 5)
(2, 4, 6)
"""
for data in ....... :
    print(data)

#%%


"""
map() & reduce()
"""
#%%
# 일반 함수
def f(x, y):
    return x + y

print(f(1, 4))

#%%
# 람다 함수
f = lambda x, y: x + y
print(f(1, 4))



#%%
# map 함수 함수와 인자(argument)를 맵핑 시켜주는 함수
f = lambda x: x**2
num = [1, 2, 3, 4, 5]
print(list(map(f, num)))

#%%
for val in map(f, num):
    print(val)

#%%
# List Comprehension : better!!
num = [1, 2, 3, 4, 5]
num2 = [i**2 for i in num]
print(num2)

#%%
# map 함수
f = lambda x,y: x + y
num = [1, 2, 3, 4, 5]
list(map(f, num, num))
list(map(f, num,num))

#%%
# map 함수 : filtering
num = [1, 2, 3, 4, 5]
num2 = list(map(lambda x:x**2 if x%2 == 0 else x, num))
print(num2)
#%%
# List Comprehension : better!
num = [1, 2, 3, 4, 5]
num2 = [x**2 if x%2 == 0 else x for x in num]
print(num2)

#%%
# 모든 수위 합
x = 0
for y in [1, 2, 3, 4, 5]:
    x += y

print(x)

#%%
# reduce 함수 
from functools import reduce
num = [1, 2, 3, 4, 5]
num2 = reduce(lambda x,y :x+y, num)
print(num2)
#%%
"""
asterisk
"""
#%%
# *
def test1(a, *args):
    print(a, args)
    print(type(args))  # <class 'tuple'>
    
test1(1, 2, 3, 4, 5)

#%%
# **
def test1(a, **args):
    print(a, args)
    print(type(args))  # <class 'dict'>
    
test1(1, b=2, c=3, d=4, f=5)
#test1(1, 2, c=3, d=4, e=5)  # error

#%%
# unpacking
def test1(a, args):
    print(a, *args)
    print(type(args))  # <class 'tuple'>
    
test1(1, (2, 3, 4, 5))

#%%
# unpacking
def test1(a, *args):
    print(a, args)
    print(type(args))  # <class 'tuple'>
    
test1(1, *(2, 3, 4, 5))

#%%
# unpacking
a, b, c = [[1,2], [3,4], [5,6]]
print(a, b, c)

#%%
# unpacking
data = [[1,2], [3,4], [5,6]]
print(data)
print(*data)
a, b, c, = data
print(a, b, c)

#%%
# unpacking
for data in zip(*[[1,2], [3,4], [5,6]]):
    print(data)
    print(type(data))
    
#%%
# unpacking
def test1(a, b, c, d):
    print(a, b, c, d)

data = {'b':2, 'c':3, 'd':4}   
test1(1, *data)
test1(1, **data)

#%%
